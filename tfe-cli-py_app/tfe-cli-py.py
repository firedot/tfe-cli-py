#!/usr/bin/env python3

import requests, urllib3

token = "Bearer " + str(input('Please enter your token: '))

# Define the main url to TFE
url = 'https://app.terraform.io/api/v2'

#Define the headers to be used
headers = {'Authorization': token , 'Content-Type': 'application/vnd.api+json'}
rget = requests.get('https://app.terraform.io/api/v2/organizations/HiveCorp/workspaces/ExtIP', headers=headers)
print(token)
print(url)
print(headers)
print(rget.status_code)
