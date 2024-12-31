import os
from my_colors import colors

def status():
    dir         = os.path.realpath('')
    dir_content = os.listdir(dir)

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