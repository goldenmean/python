'''
import platform
#print(platform.system())
#print(platform.python_revision())
#print(platform.python_version())
#print(platform.version())
#print(dir(platform.sys))
#print(platform.architecture())
#print(platform.machine())
'''

'''
import requests

url = 'https://www.w3schools.com/python/demopage.php'
myobj = {'somekey': 'somevalue'}

#x = requests.post(url, json = myobj)
x=requests.get(url)
#print the response text (the content of the requested file):
#print(x.text)
#help(x)
#print(x.status_code)
#print(x.json)
#print(x.headers)
print(x.text)
'''

import subprocess
'''
command: The command to be executed (in this case, "dir").
capture_output=True: Capture the output of the command instead of printing it to the console.
text=True: Return the output as a string instead of bytes.
shell=True: Execute the command through the shell, allowing for more complex commands and shell features.
The result is stored in the res variable, which contains information about the command's execution,
including the output (accessible via res.stdout
'''
command = "dir"
res=subprocess.run(command,capture_output=True, text=True, shell=True)
print(res.stdout)