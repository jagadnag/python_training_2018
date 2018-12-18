#!/usr/bin/env python
from netmiko import ConnectHandler

# SSH Connection Details
ios_devices = {
    'device_type': 'cisco_ios',
    'ip': '172.21.56.120',
    'username': 'cisco',
    'password': 'cisco',
}

# Establish SSH to device and run show command
net_connect = ConnectHandler(**ios_devices)
output = net_connect.send_config_set('logging host 1.1.1.1')
print output