#!/usr/bin/env python3

import sys
import requests

def fetch_x_request_id(url):
    """
    Fetches the value of the 'X-Request-Id' variable from the response header.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for HTTP errors (status codes >= 400)
        
        x_request_id = response.headers.get('X-Request-Id')
        if x_request_id:
            print("X-Request-Id:", x_request_id)
        else:
            print("X-Request-Id not found in the response headers.")
    except requests.RequestException as e:
        print("Error fetching data:", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    fetch_x_request_id(url)
