#!/usr/bin/env python3

import sys
import requests

def send_post_request(url, email):
    """
    Sends a POST request to the URL with the email as a parameter and displays the body of the response.
    """
    try:
        data = {'email': email}
        response = requests.post(url, data=data)
        print("Response body:")
        print(response.text)
    except requests.RequestException as e:
        print("Error sending POST request:", e)

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    send_post_request(url, email)
