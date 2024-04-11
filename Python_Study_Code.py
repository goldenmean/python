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
command = "dir"
res=subprocess.run(command,capture_output=True, text=True, shell=True)
print(res.stdout)