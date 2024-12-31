import os

def add(path: str):
    dir_path     = os.path.realpath(path)
    dir_content  = os.listdir(dir_path)
    geet_dir     = os.path.join(dir_path, '.geet')
    tracked_file = os.path.join(geet_dir, 'tracked.txt') 

    if not os.path.exists(geet_dir):
        os.mkdir(geet_dir)

    geet_dir_content = os.listdir(geet_dir)

    if 'tracked.txt' not in geet_dir_content:
        os.path.join(geet_dir, 'tracked.txt')

    try:
        with open(tracked_file, 'w') as file:
            for file_name in dir_content:
                file.write(file_name + '\n')
    except:
        print('Invalid path')
        exit()