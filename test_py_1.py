from dotenv import load_dotenv
import os

load_dotenv()

domain = os.getenv('DOMAIN')
email = os.getenv('ADMIN_EMAIL')
rooturl = os.getenv('ROOT_URL')

print(f"domain is {domain}")
print(f"email is {email}")
print(f"rooturl is {rooturl}")


# from dotenv import dotenv_values
# config = dotenv_values(".env")
# print(config)