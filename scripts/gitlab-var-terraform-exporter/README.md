# Gitlab variable terraform exporter

## Description
Export and convert variables from Gitlab project to terraform tfvar file

## Requirements
- Gitlab token with permissions to read project variables;
- `GITLAB_API_PRIVATE_TOKEN` environment variable;
- Gitlab hostname;
- Gitlab project ID;
- `TFVAR` output file;

## Usage

```shell
$ python gitlab-var-terraform-exporter.py -h
usage:
    python script_name.py --host <gitlabhost> --project <project_id> --output <output_file>

Fetch GitLab variables and create Terraform .tfvars.tf file

options:
  -h, --help         show this help message and exit
  --host HOST        GitLab host URL
  --project PROJECT  GitLab project ID
  --output OUTPUT    Output file name for .tfvars.tf
```

```shell
$ python gitlab-var-exporter.py --host https://host.gitlab.com --project 555 --output converted_variables.tfvars.tf
```
