# Bibucket cloner

This script helps you clone multiple repositories from Bitbucket based on criterias.
Available filters:

* bitbucket repository name using API filter or regular expression
* bitbucket project name using API filter

The script uses the [Bitbucket cloud API](https://developer.atlassian.com/bitbucket/api/2/reference/resource/repositories) for repositories 

Prefer -p & -nc over -re since the last one is a local filter (download the repository list first, then applies filter).

## Requirements

python 3.x

## Installation

`pip install -r requirements.txt`

## Usage

`python clone_repositories username_or_team_name`

### Help

```bash
usage: clone_repositories.py [-h] [-p PROJECT] [-nc NAME_CONTAINS] [-re REGULAR_EXPRESSION] [-u USERNAME] [-o OUTPUT_FOLDER] [-cm {ssh,https}] team

Clone multiple bitbucket repositories. This script only support git repositories.

positional arguments:
  team                  bitbucket team or username

optional arguments:
  -h, --help            show this help message and exit
  -p PROJECT, --project PROJECT
                        filter repositories based on bibucket project name. API filter
  -nc NAME_CONTAINS, --name-contains NAME_CONTAINS
                        filter repositories based on case-insensitive repository name contains text. API filter
  -re REGULAR_EXPRESSION, --regular-expression REGULAR_EXPRESSION
                        filter repositories based on bitbucket repository name using a regular expression. This filter is applied after getting the list of repositories.
  -u USERNAME, --username USERNAME
                        bitbucket account username used to clone repositories list, will use team if not provided.
  -o OUTPUT_FOLDER, --output-folder OUTPUT_FOLDER
                        output folder, where to clone repositories.
  -cm {ssh,https}, --clone-method {ssh,https}
                        cloning method, ssh or https. Both methods assumes that your bitbucket credentials are defined system wide.
```