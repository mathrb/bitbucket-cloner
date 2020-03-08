import argparse
import getpass
import re
import os

import requests

parser = argparse.ArgumentParser(description='Clone multiple bitbucket repositories. This script only support git repositories.')

parser.add_argument('team', help='bitbucket team or username')
parser.add_argument('-re', '--regular-expression', help='filter repositories based on bitbucket repository name using a regular expression.', default=None)
parser.add_argument('-p', '--project', help='filter repositories based on bibucket project name.')
parser.add_argument('-u', '--username', help='bitbucket account username used to clone repositories list, will use team if not provided.', default=None)
parser.add_argument('-o', '--output-folder', help='output folder, where to clone repositories.', default=None)
parser.add_argument('-cm', '--clone-method', choices=['ssh', 'https'], help='cloning method, ssh or https. Both methods assumes that your bitbucket credentials are defined system wide.', default='ssh')

args = parser.parse_args()

base_url = "https://api.bitbucket.org/2.0/repositories/{}?pagelen=100".format(args.team)
username = args.team if args.username is None else args.username
password = getpass.getpass('bitbucket password: ')

response = requests.get(base_url, auth=(username, password))
if response.status_code != 200:
    print("{}: {}.{}".format(response.status_code, response.reason, response.text))
    exit()

response = response.json()
repositories = response

def clone_repositories(repositories):
    for rep in repositories:
        if args.pattern is not None and not re.match(args.pattern, rep["name"]):
            continue
        clone_link = [link["href"] for link in rep["links"]["clone"] if link["name"] == args.clone_method]
        if clone_link:
            command = "git clone " + clone_link[0]
            if args.output_folder is not None:
                command += " {}".format(os.path.join(args.output_folder, rep["name"]))
            os.system(command)

clone_repositories(response["values"])
while "next" in response and response["next"] is not None:
    response = requests.get(response["next"], auth=(username, password)).json()
    clone_repositories(response["values"])
