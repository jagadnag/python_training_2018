#!/usr/bin/env python
 
from netmiko import ConnectHandler

# Sending multiple lines of config stored in a file 
with open('basic_config') as f:
    commands_to_send = f.read().splitlines()

# SSH Connection details 

ios_router = {
    'device_type': 'cisco_ios',
    'ip': '172.21.56.120',
    'username': 'cisco',
    'password': 'cisco',
}

all_devices = [ios_router]

# Iterate through device list and configure the devices  
for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(commands_to_send)
    print output