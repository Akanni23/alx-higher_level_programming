#!/usr/bin/env python3

import urllib.request
import sys

def get_x_request_id(url):
    """
    Fetches the value of the 'X-Request-Id' variable from the header of the response.
    """
    try:
        with urllib.request.urlopen(url) as response:
            x_request_id = response.headers.get('X-Request-Id')
            if x_request_id:
                print("X-Request-Id:", x_request_id)
            else:
                print("X-Request-Id not found in the response headers.")
    except Exception as e:
        print("Error fetching data:", e)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        url = sys.argv[1]
        get_x_request_id(url)
    else:
        print("Usage: python script.py <URL>")
