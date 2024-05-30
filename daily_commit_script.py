import os
import subprocess
import requests
from datetime import datetime

# Configuration
REPO_PATH = 'D:\Projects\DailyCommitScript' # path to your repository path
FILE_PATH = os.path.join(REPO_PATH, 'daily_commit.txt')
COMMIT_MESSAGE = f'Daily quote: {datetime.now().date()}'
BRANCH_NAME = 'main'  # Update this to your branch name if different

def get_quote():
    response = requests.get('https://api.quotable.io/random')
    if response.status_code == 200:
        return response.json()['content']
    else:
        return 'Could not fetch a quote today.'

def main():
    # Change to the repository directory
    os.chdir(REPO_PATH)
    
    # Get a random quote and save it to the file
    quote = get_quote()
    with open(FILE_PATH, 'a') as f:
        f.write(f'{datetime.now()} - {quote}\n')
    
    # Stage the changes
    os.system('git add .')
    
    # Commit the changes
    os.system(f'git commit -m "{COMMIT_MESSAGE}"')
    
    # Push the changes
    os.system(f'git push origin {BRANCH_NAME}')

if __name__ == '__main__':
    main()