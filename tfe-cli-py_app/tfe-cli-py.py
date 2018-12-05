#!/usr/bin/env python3

import requests, urllib3

token = "Bearer " + str(input('Please enter your token: '))
organization_name = str(input('Please enter your organization name: '))
workspace_name = str(input('Please enter your worksapce name: '))
# Define the main url to TFE
url = 'https://app.terraform.io/api/v2/'

rget = requests.get
# Variable containing the ID of your workspace
wspace_id_url = str(url + 'organizations/' + organization_name + '/workspaces/' + workspace_name)


#payload={'Organization': 'HiveCorp', 'workspace': 'ExtIP'}
#Define the headers to be used
headers = {'Authorization': token , 'Content-Type': 'application/vnd.api+json'}
wspace_id = rget( wspace_id_url , headers=headers)

print(wspace_id_url)
print(wspace_id.status_code)

print(wspace_id.text)
print(wspace_id.url)
