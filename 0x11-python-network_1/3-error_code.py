#!/usr/bin/env python3

import sys
import urllib.request
import urllib.error

def fetch_url(url):
    """
    Fetches the content from the URL and displays it.
    """
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
    except Exception as e:
        print("Error fetching data:", e)

if __name__ == "__main__":
    url = sys.argv[1]
    fetch_url(url)
