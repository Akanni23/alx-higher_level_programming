#!/usr/bin/env python3

import sys
import requests

def fetch_url(url):
    """
    Fetches the content from the given URL and displays it.
    """
    try:
        response = requests.get(url)
        if response.status_code >= 400:
            print("Error code:", response.status_code)
        else:
            print(response.text)
    except requests.RequestException as e:
        print("Error fetching data:", e)

if __name__ == "__main__":
    url = sys.argv[1]
    fetch_url(url)
