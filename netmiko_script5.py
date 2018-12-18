#!/usr/bin/env python
 
from netmiko import ConnectHandler
from getpass import getpass

# SSH username and password provided by user
username = raw_input('Enter your SSH username: ')
password = getpass()

# Sending list of show commands stored in a file 
with open('show_command') as f:
    show_commands = f.readlines()

# Sending device ip's stored in a file 
with open('devices_list') as f:
    devices_list = f.read().splitlines()

# Iterate through device list 
for devices in devices_list:
    print 'Connecting to device ' + devices
    ip_address_of_device = devices
    
    # SSH Connection details
    ios_router = {
        'device_type': 'cisco_ios',
        'ip': ip_address_of_device, 
        'username': username,
        'password': password
    }
    # Iterate through show command list
    net_connect = ConnectHandler(**ios_router)
    for command in show_commands:
        output = net_connect.send_command(command)
        print command + output + '\n'