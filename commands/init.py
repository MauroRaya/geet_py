import os
import subprocess

def init():
    folder_name = '.geet'
    os.mkdir(folder_name)
    
    if os.name == 'nt':  # Check if the OS is Windows
        subprocess.call(['attrib', '+H', folder_name])