import os
import datetime

# Define the fireworks pattern
fireworks = [
    "   X   ",  
    "  X X  ",  
    " X   X ",  
    "X  X  X",  
    " X   X ",  
    "  X X  ",  
    "   X   "
]

# Set the starting date for commits
start_date = datetime.date(2024, 1, 1)

# Loop through the pattern and create commits
for i, row in enumerate(fireworks):
    for j, cell in enumerate(row):
        if cell == 'X':  # If this position should have a commit
            commit_date = start_date + datetime.timedelta(days=j + (i * 7))  
            os.system(f'GIT_COMMITTER_DATE="{commit_date}" git commit --allow-empty -m "Fireworks commit" --date="{commit_date}"')
            os.system('git push')  # Push commit to GitHub
