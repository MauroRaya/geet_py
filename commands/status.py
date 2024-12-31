import os
import sys
from my_colors import colors

def status():
    dir_path           = os.path.realpath('')
    dir_content        = os.listdir(dir_path)
    tracked_file       = os.path.join(dir_path, '.geet\\tracked.txt')
    tracked: list[str] = []

    # Populate tracked list
    try:
        with open(tracked_file) as file:
            for line in file:
                tracked.append(line.strip('\n'))
    except:
        print('Error: Unable to open file')
        sys.exit(1)

    print(colors.RESET)
    print('Untracked files:')

    # Show untracked files
    for file_name in dir_content:
        if file_name not in tracked:
            print(colors.RED + file_name)

    print(colors.RESET)
    print('Tracked files:')

    # Show tracked files
    if tracked:    
        for file_name in tracked:
            print(colors.GREEN + file_name)
    else:
        print('No files are being tracked')
        
    print(colors.RESET)