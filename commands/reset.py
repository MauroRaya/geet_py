import os

def reset():
    dir_path     = os.path.realpath('')
    geet_dir     = os.path.join(dir_path, '.geet')
    tracked_file = os.path.join(geet_dir, 'tracked.txt')

    if not os.path.exists(geet_dir):
        os.mkdir(geet_dir)
    
    if not os.path.exists(tracked_file):
        os.path.join(geet_dir, 'tracked.txt')
    
    open(tracked_file, "w").close()