import requests
import json
from bs4 import BeautifulSoup

def parse_unknown_response(url):
    response = requests.get(url)
    
    # Check the Content-Type header
    content_type = response.headers.get('Content-Type', '').lower()

    if 'application/json' in content_type:
        # If it's JSON, parse it
        try:
            return response.json()
        except json.JSONDecodeError:
            print("Content-Type says it's JSON, but parsing failed.")
    
    elif 'text/html' in content_type:
        # If it's HTML, use BeautifulSoup to parse it
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    
    elif 'text/xml' in content_type or 'application/xml' in content_type:
        # If it's XML, use BeautifulSoup with 'xml' parser
        soup = BeautifulSoup(response.text, 'xml')
        return soup
    
    elif 'text/plain' in content_type:
        # If it's plain text, return it as is
        return response.text
    
    else:
        # If we can't determine the type, try to parse as JSON first
        try:
            return response.json()
        except json.JSONDecodeError:
            # If JSON parsing fails, return the raw text
            return response.text

# Example usage
#
url = "https://jsonplaceholder.typicode.com/posts"
parsed_data = parse_unknown_response(url)
print(type(parsed_data))
print(parsed_data)