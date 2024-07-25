

from dotenv import load_dotenv
from dotenv import set_key
import os

#load_dotenv()
#API_KEY = os.getenv('OPENAI_API_KEY')
#print(API_KEY)


os.environ['WEATHER_API_KEY'] = '1234567890abcdef'
#os.putenv('WEATHER_API_KEY', '1234567890abcdef')
#print(os.getenv('WEATHER_API_KEY'))

set_key('.env', 'MYTESTPATH', 'D:/ajit')

#Read .env file variables using getenv
load_dotenv()
testpath = os.getenv('MYTESTPATH')
print(testpath)

#read .env file using file read function
#with open(".env", "r") as f:
#    print(f.read())



'''
from dotenv import dotenv_values, set_key


# Load the existing .env file
env_values = dotenv_values(".env")

#print(env_values)

# Update the dictionary with the new value
env_values["MYTESTPATH"] = "D:/ajit"

# Write the updated dictionary back to the .env file
with open(".env", "w") as f:
    for key, value in env_values.items():
        f.write(f"{key}={value}\n")


# Verify that the value was written to the .env file
with open(".env", "r") as f:
    print(f.read())

'''
