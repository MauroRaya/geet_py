import os
import subprocess
from my_colors import colors

tracked = []

def geet_init():
    folder_name = '.geet'
    os.mkdir(folder_name)
    
    if os.name == 'nt':  # Check if the OS is Windows
        subprocess.call(['attrib', '+H', folder_name])


def geet_add(path: str):
    try:
        for file_name in path:
            tracked.append(file_name)
    except:
        print('Invalid path')
        exit()


def geet_status():
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
    for file_name in tracked:
        print(colors.GREEN + file_name)

    print(colors.RESET)


geet_status()
