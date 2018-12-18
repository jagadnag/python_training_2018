#!/usr/bin/env python
from netmiko import ConnectHandler
from datetime import date

# SSH Connection Details
ios_devices = {
    'device_type': 'cisco_ios',
    'ip': '172.21.56.120',
    'username': 'cisco',
    'password': 'cisco',
}

# Establish SSH to device and run show command
net_connect = ConnectHandler(**ios_devices)
net_connect.send_command('terminal length 0')
output = net_connect.send_command('show running-config')
print output
saveoutput = open('cfgbackup_' + ios_devices['ip'] + '_' + str(date.today()), 'w')
saveoutput.write(output)
saveoutput.close