#!/usr/bin/env python3

import urllib.parse
import urllib.request
import sys

def send_post_request(url, email):
    """
    Sends a POST request to the URL with the email as a parameter and displays the body of the response.
    """
    try:
        # Encode the data
        data = urllib.parse.urlencode({'email': email}).encode('utf-8')
        
        # Send the POST request
        with urllib.request.urlopen(url, data=data) as response:
            # Decode and print the body of the response
            print(response.read().decode('utf-8'))
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    send_post_request(url, email)
