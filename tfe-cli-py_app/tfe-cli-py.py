#!/usr/bin/env python3

import urllib.request, json

#token = "Bearer " + str(input('Please enter your token: '))
token = "Bearer " + 
#organization_name = str(input('Please enter your organization name: '))
organization_name = 'HiveCorp'
#workspace_name = str(input('Please enter your worksapce name: '))

# Define the main url to TFE
url = 'https://app.terraform.io/api/v2/'

#rget = requests.get

# Variable containing the ID of your workspace
#wspace_id_url = str(url + 'organizations/' + organization_name + '/workspaces/' + workspace_name)
org_workspaces_url = str(url + 'organizations/' + organization_name + '/workspaces/')
#payload={'Organization': 'HiveCorp', 'workspace': 'ExtIP'}

#Define the headers to be used

header_1 = {'key' : 'Authorization', 'value' : token }
header_2 = {'key' : 'Content-Type', 'value' : 'application/vnd.api+json'}


#print(org_workspaces_url)
# Create an URL to request all workspaces within the given Organization
wspaces_request = urllib.request.Request(org_workspaces_url)

# Attach headers to the URL created
wspaces_request.add_header(header_1['key'], header_1['value'])
wspaces_request.add_header(header_2['key'], header_2['value'])


# Gather workspaces information
with urllib.request.urlopen(wspaces_request) as connection:
   org_wspaces_inf =  connection.read()


# Count how many workspaces are available
workspaces_count = str(org_wspaces_inf).count('name')
workspaces_list = []
for i in range(workspaces_count):
    workspaces_list.append(json.loads(org_wspaces_inf)['data'][i]['attributes']['name'])

#print(workspaces_list)

#for workspace in workspaces_list:
#    print(workspace)

def return_menu_option(options_list):
    """
    (list) -> str
    A function that creates a menu from a list.
    Returns the value of the option chosen by the user.

    >>> return_menu_option(['apple', 'pear' 'banana'])

    """
    for i in range(len(options_list)):
        for option in options_list:
            print('[{0}]'.format(i), option)
        break
    choice = 'empty'
    while lower.choice != 'quit':
        choice = input(str("Please choose an option by entering a number between 1 and {0} or 'quit' to exit: ".format(len(options_list))))
        if choice.lower == 'quit':
            print('Exiting...')
        elif int(choice) in range(len(options_list)):
            for i in range(len(options_list)):
                if int(choice) == i:
                    return options_list[i]
                else:
                    continue

        else:
            print("Invalid option.")
            print("Try again...")
            continue

selected_workspace = return_menu_option(workspaces_list)
