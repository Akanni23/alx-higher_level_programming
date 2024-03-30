#!/usr/bin/env python3

import sys
import requests

def search_user(letter):
    """
    Sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.
    """
    try:
        url = "http://0.0.0.0:5000/search_user"
        data = {'q': letter}
        response = requests.post(url, data=data)
        response.raise_for_status()  # Raise an error for HTTP errors (status codes >= 400)
        
        print(response.text)
    except requests.RequestException as e:
        print("Error sending POST request:", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <letter>")
        sys.exit(1)

    letter = sys.argv[1]
    search_user(letter)
