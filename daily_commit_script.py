import os
import subprocess
from datetime import datetime

# Configuration
REPO_PATH = 'D:\Projects\DailyCommitScript' # path to your repository path
FILE_PATH = os.path.join(REPO_PATH, 'daily_commit.txt')
COMMIT_MESSAGE = 'Daily commit'
BRANCH_NAME = 'main'  # Change to your branch name

def main():
    # Change to the repository directory
    os.chdir(REPO_PATH)
    
    # Modify or create the file
    with open(FILE_PATH, 'a') as f:
        f.write(f'Daily commit at {datetime.now()}\n')
    
    # Stage the changes
    subprocess.run(['git', 'add', FILE_PATH], check=True)
    
    # Commit the changes
    subprocess.run(['git', 'commit', '-m', COMMIT_MESSAGE], check=True)
    
    # Push the changes
    subprocess.run(['git', 'push', 'origin', BRANCH_NAME], check=True)

if __name__ == '__main__':
    main()
