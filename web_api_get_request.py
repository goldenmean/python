"""
Using python requests and jsom module to make a GET request to a web api 
and get the response as a list of todos for a given user.
"""

import requests
import json

def get_todos(user_id):
    # API endpoint URL
    url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"

    try:
        # Send GET request to the API
        response = requests.get(url)
        print(f"Response received with status code {response.status_code}")
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            todos = response.json()
            return todos
        else:
            print(f"Error: Received status code {response.status_code}")
            return None

    except requests.RequestException as e:
        print(f"Error occurred while making the request: {e}")
        return None

def main():
    user_id = 1
    todos = get_todos(user_id)

    if todos:
        print(f"Todos for user {user_id}:")
        for todo in todos:
            print(todo)
            #print(f"- {todo['title']} ({'Completed' if todo['completed'] else 'Not Completed'})")
    else:
        print("Failed to retrieve todos.")

if __name__ == "__main__":
    main()