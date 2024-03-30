#!/usr/bin/env python3

import requests

def fetch_status():
    """
    Fetches the content from the URL https://alx-intranet.hbtn.io/status using requests and displays it.
    """
    try:
        response = requests.get("https://alx-intranet.hbtn.io/status")
        response.raise_for_status()  # Raise an error for HTTP errors (status codes >= 400)
        print("Body response:")
        print("\t- type:", type(response.text))
        print("\t- content:", response.text)
    except requests.RequestException as e:
        print("Error fetching data:", e)

if __name__ == "__main__":
    fetch_status()
