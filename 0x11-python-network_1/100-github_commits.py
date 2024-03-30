
#!/usr/bin/env python3

import sys
import requests

def fetch_commits(repo_owner, repo_name, num_commits=10):
    """
    Fetches the specified number of most recent commits from a GitHub repository and prints them.
    """
    try:
        url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits"
        params = {'per_page': num_commits}
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an error for HTTP errors (status codes >= 400)

        commits = response.json()
        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    except requests.RequestException as e:
        print("Error fetching data:", e)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <repo_owner> <repo_name>")
        sys.exit(1)

    repo_owner = sys.argv[1]
    repo_name = sys.argv[2]
    fetch_commits(repo_owner, repo_name)
