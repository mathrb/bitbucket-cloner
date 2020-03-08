# Bibucket cloner

This script helps you clone multiple repositories from Bitbucket based on criterias.
Available filters:

* regular expression applied on name of repositories
* bitbucket project name

The script uses the [Bitbucket cloud API](https://developer.atlassian.com/bitbucket/api/2/reference/resource/repositories) for repositories 

## Requirements

python 3.x

## Installation

`pip install -r requirements.txt`

## Usage

`python clone_repositories username_or_team_name`

### Help

```bash
usage: clone_repositories.py [-h] [-re REGULAR_EXPRESSION] [-p PROJECT] [-u USERNAME] [-o OUTPUT_FOLDER] [-cm {ssh,https}] team

Clone multiple bitbucket repositories. This script only support git repositories.

positional arguments:
  team                  bitbucket team or username

optional arguments:
  -h, --help            show this help message and exit
  -re REGULAR_EXPRESSION, --regular-expression REGULAR_EXPRESSION
                        filter repositories based on bitbucket repository name using a regular expression.
  -p PROJECT, --project PROJECT
                        filter repositories based on bibucket project name.
  -u USERNAME, --username USERNAME
                        bitbucket account username used to clone repositories list, will use team if not provided.
  -o OUTPUT_FOLDER, --output-folder OUTPUT_FOLDER
                        output folder, where to clone repositories.
  -cm {ssh,https}, --clone-method {ssh,https}
                        cloning method, ssh or https. Both methods assumes that your bitbucket credentials are defined system wide.
```