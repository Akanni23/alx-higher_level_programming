#!/usr/bin/env python3
"""
Fetches the content of a URL using urllib and prints it.
"""

import urllib.request

def fetch_status():
    """
    Fetches the status from the URL.
    """
    url = "https://alx-intranet.hbtn.io/status"
    try:
        with urllib.request.urlopen(url) as response:
            print("Body response:")
            print("\t- type:", type(response.read()))
            print("\t- content:", response.read().decode('utf-8'))
    except Exception as e:
        print("Error fetching data:", e)

if __name__ == "__main__":
    fetch_status()
