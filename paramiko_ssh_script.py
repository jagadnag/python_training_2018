#!/usr/bin/env python

import paramiko
import time
import getpass

ip_address = "172.21.56.120"
username = raw_input("Enter your SSH username: ")
password = getpass.getpass()

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address, username=username,
                   password=password, allow_agent=False, look_for_keys=False)

print "Successful connection", ip_address

remote_connection = ssh_client.invoke_shell()

remote_connection.send("configure terminal\n")
time.sleep(1)
print "Configuring Loopback Interface 101"
remote_connection.send("interface loopback 0\n")
remote_connection.send("ip address 101.1.1.1 255.255.255.255\n")
time.sleep(1)
remote_connection.send("end\n")

time.sleep(1)
output = remote_connection.recv(65535)
print output

ssh_client.close