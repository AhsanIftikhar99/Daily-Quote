import os
import subprocess
import requests
from datetime import datetime

# Configuration
REPO_PATH = 'D:\\Projects\\DailyCommitScript'  # Use double backslashes or raw strings for Windows paths
FILE_PATH = os.path.join(REPO_PATH, 'daily_commit.txt')
COMMIT_MESSAGE = 'Daily commit'
BRANCH_NAME = 'main'  # Change to your branch name
QUOTE_API_URL = 'https://api.quotable.io/random'

def get_quote():
    try:
        response = requests.get(QUOTE_API_URL)
        response.raise_for_status()
        data = response.json()
        return f"{data['content']} — {data['author']}"
    except requests.RequestException as e:
        print(f"Failed to fetch quote: {e}")
        return None

def main():
    # Change to the repository directory
    os.chdir(REPO_PATH)

    # Get a new quote
    quote = get_quote()
    if not quote:
        quote = 'No quote available'

    # Modify or create the file
    with open(FILE_PATH, 'a') as f:
        f.write(f'Daily commit at {datetime.now()}\n')
        f.write(f'Quote of the day: {quote}\n\n')

    # Stage the changes
    subprocess.run(['git', 'add', FILE_PATH], check=True)

    # Commit the changes
    commit_message = f"{COMMIT_MESSAGE}: {quote}"
    subprocess.run(['git', 'commit', '-m', commit_message], check=True)

    # Push the changes
    subprocess.run(['git', 'push', 'origin', BRANCH_NAME], check=True)

if __name__ == '__main__':
    main()
