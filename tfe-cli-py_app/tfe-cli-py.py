#!/usr/bin/env python3

import urllib.request, json

token = "Bearer " + str(input('Please enter your token: '))
organization_name = str(input('Please enter your organization name: '))

"""
# The following lines are left for development purposes. Should be removed in
# the final version


token = "Bearer " + ''
organization_name = 'HiveCorp'
workspace_name = str(input('Please enter your worksapce name: '))
"""

# Define the main url to TFE
url = 'https://app.terraform.io/api/v2/'

# Compose URL from which worskpaces should be obtained.
org_workspaces_url = str(url + 'organizations/' + organization_name + '/workspaces/')

#Define the headers to be used

header_1 = {'key' : 'Authorization', 'value' : token }
header_2 = {'key' : 'Content-Type', 'value' : 'application/vnd.api+json'}


# Create a request to obtain all workspaces for a given organization (output
# depends on the permissions your user has)
wspaces_request = urllib.request.Request(org_workspaces_url)

# Attach headers to the prevuously created request
wspaces_request.add_header(header_1['key'], header_1['value'])
wspaces_request.add_header(header_2['key'], header_2['value'])


# Gather workspaces information
with urllib.request.urlopen(wspaces_request) as connection:
   org_wspaces_inf =  connection.read()


# Count how many workspaces are available
workspaces_count = str(org_wspaces_inf).count('name')

# Create a list with the available workspaces

workspaces_list = []
for i in range(workspaces_count):
    workspaces_list.append(json.loads(org_wspaces_inf)['data'][i]['attributes']['name'])

def return_menu_option(options_list):
    """
    (list) -> str
    A function that creates a menu from a list.
    Returns the value of the option chosen by the user.

    >>> return_menu_option(['apple', 'pear' 'banana'])
    [1] apple
    [2] pear
    [3] banana
    Please choose an option by entering a number between 1 and 3 or 'quit' to exit: 1

    >>> return_menu_option(['apple', 'pear' 'banana'])
    [1] apple
    [2] pear
    [3] banana
    Please choose an option by entering a number between 1 and 3 or 'quit' to exit: quit
    Exiting...

    """
    for i in range(1, len(options_list) + 1):
        print('[{0}]'.format(i), options_list[i - 1])
    choice = 'empty'
    while choice.lower() != 'quit':
        choice = input(str("Please choose an option by entering a number between 1 and {0} or 'quit' to exit: ".format(len(options_list))))
        if choice.lower() == "quit":
            print('Exiting...')
            break
        elif len(choice) > 1:
            print("Invalid option!")
            print("Try again.")
            continue
        elif int(choice) in range(1, len(options_list) + 1):
            for i in range(1, len(options_list) + 1):
                if int(choice) == i:
                    return options_list[i-1]
                else:
                    continue

        else:
            print("Invalid option.")
            print("Try again...")

# The following code is left for debugging purposes. Should be removed in the
# final version. 
selected_workspace = return_menu_option(workspaces_list)

print(selected_workspace, type(selected_workspace))
