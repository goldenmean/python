'''
To launch a script on two different computers at the exact same time, you can use the
 Network Time Protocol (NTP) to synchronize the system clocks of the computers and 
 then schedule the script to run at a precise time. Here's a simple approach using 
 Python and SSH:

Ensure both computers are synchronized using NTP.
Use paramiko (a Python library for SSH) to connect and execute the script on both 
computers.
'''

import paramiko
import time

def synchronize_and_execute(host, username, password, command, execution_time):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host, username=username, password=password)

    # Schedule the command to run at the specified time
    schedule_command = f'echo "{command}" | at {execution_time}'
    
    stdin, stdout, stderr = client.exec_command(schedule_command)
    print(stdout.read().decode())
    print(stderr.read().decode())
    
    client.close()

# Details for the remote computers
hosts = [
    {"host": "192.168.1.2", "username": "user1", "password": "password1"},
    {"host": "192.168.1.3", "username": "user2", "password": "password2"}
]

# Command to execute
command = "/path/to/your/script.sh"

# Define the execution time in HH:MM format
execution_time = (time.strftime("%H:%M", time.gmtime(time.time() + 60)))  # 1 minute from now

# Synchronize and execute the command on each host
for host in hosts:
    synchronize_and_execute(host["host"], host["username"], host["password"], command, execution_time)