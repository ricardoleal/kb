##############################################################################
# Export and convert variables from Gitlab project to terraform tfvar file
# mail@ricardoleal.me
#
# Requirements:
# - ENV-VAR: GITLAB_API_PRIVATE_TOKEN
# - Gitlab hostname (defaults to gitlab.com)
# - Gitlab project ID
# - TFVAR output file
#
# Usage:
# python gitlab-var-terraform-exporter.py --host https://host.gitlab.com --project 555 --output converted_variables.tfvars.tf
##############################################################################
import os
import argparse
import requests

def fetch_variables_from_gitlab(api_url, project_id, token):
    headers = {'Private-Token': token}
    url = f"{api_url}/api/v4/projects/{project_id}/variables"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch variables. Status code: {response.status_code}")
        return None

def write_tfvars_tf(variables, file_path):

    with open(file_path, 'w') as file:
        file.write('# File generated from gitlab variables\n')
        for variable in variables:
            print(f" > {variable['key']}")
            if variable['value'].isnumeric() or variable["value"] == "True" or variable["value"] == "False":
                file.write('{key} = {value}\n'.format(key=variable["key"], value=variable["value"]))
            elif '\n' in variable["value"]:
                file.write('{key} = <<-EOT\n{value}EOT\n'.format(key=variable["key"], value=variable["value"]))
            else:
                file.write('{key} = "{value}"\n'.format(key=variable["key"], value=variable["value"]))

def main():
    usage = """
    Usage:
    python gitlab-var-terraform-exporter.py --host <gitlabhost> --project <project_id> --output <output_file>
    Example:
    python gitlab-var-terraform-exporter.py --host https://host.gitlab.com --project 555 --output converted_variables.tfvars.tf
    """
    parser = argparse.ArgumentParser(description='Fetch GitLab variables and create Terraform .tfvars.tf file',usage=usage)
    parser.add_argument('--host', help='GitLab host URL', required=True)
    parser.add_argument('--project', help='GitLab project ID', required=True)
    parser.add_argument('--output', help='Output file name for .tfvars.tf', required=True)
    args = parser.parse_args()

    api_url = args.host
    project_id = args.project
    output_file = args.output
    token = os.getenv('GITLAB_API_PRIVATE_TOKEN')

    if token is None:
        print("GITLAB_API_PRIVATE_TOKEN environment variable is not set.")
        return

    variables = fetch_variables_from_gitlab(api_url, project_id, token)

    if variables:
        write_tfvars_tf(variables, output_file)
        print(f"All variables written to {output_file}")
    else:
        print("Failed to fetch variables from GitLab.")

if __name__ == "__main__":
    main()
