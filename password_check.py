# Ways to read a password stored locally for comparison

import os
import getpass

STORED_PASSWORD = os.environ.get('MY_APP_PASSWORD')
password = getpass.getpass('Enter your password: ')
if password != STORED_PASSWORD:
    print('Access Denied')
    exit()

# using configparser

import configparser
import getpass

config = configparser.ConfigParser()
config.read('config.ini')
STORED_PASSWORD = config['Security']['password']

# use a stored password hash file
import hashlib
import getpass

def verify_password(password):
    with open('password.hash', 'r') as hash_file:
        stored_hash = hash_file.read().strip()
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    return password_hash == stored_hash


# Use encrypted file which stores the encrypted password and a decryption key file
from cryptography.fernet import Fernet
import getpass

def get_stored_password():
    with open('key.key', 'rb') as key_file:
        key = key_file.read()
    f = Fernet(key)
    with open('password.enc', 'rb') as password_file:
        encrypted_password = password_file.read()
    return f.decrypt(encrypted_password).decode()

STORED_PASSWORD = get_stored_password()