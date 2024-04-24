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

### Requirements install
```shell
$ pip3 install -r requirements.txt
```

### Help
```shell
$ python gitlab-var-terraform-exporter.py -h
usage:
    python gitlab-var-terraform-exporter.py --host <gitlabhost> --project <project_id> --output <output_file>
example:
    python gitlab-var-terraform-exporter.py --host https://host.gitlab.com --project 555 --output converted_variables.tfvars.tf

Fetch GitLab variables and create Terraform .tfvars.tf file

options:
  -h, --help         show this help message and exit
  --host HOST        GitLab host URL
  --project PROJECT  GitLab project ID
  --output OUTPUT    Output file name for .tfvars.tf
```
### Running
```shell
$ python gitlab-var-exporter.py --host https://host.gitlab.com --project 555 --output converted_variables.tfvars.tf
```
