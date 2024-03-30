#!/usr/bin/env python3

import sys
import requests
from requests.auth import HTTPBasicAuth

def get_user_id(username, password):
    """
    Fetches the user ID using GitHub API with provided credentials.
    """
    try:
        # Make a GET request to the GitHub API to fetch user details
        response = requests.get('https://api.github.com/user', auth=HTTPBasicAuth(username, password))
        
        # Check if the request was successful
        if response.status_code == 200:
            user_data = response.json()
            user_id = user_data['id']
            print("Your GitHub user ID is:", user_id)
        elif response.status_code == 401:
            print("Unauthorized: Invalid credentials.")
        else:
            print("Error: Failed to fetch user ID. Status code:", response.status_code)
    except requests.RequestException as e:
        print("Error fetching data:", e)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <username> <password>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    get_user_id(username, password)
