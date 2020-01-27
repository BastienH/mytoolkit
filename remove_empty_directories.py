import os

os.chdir(r"C:\Users\NG8203C\Desktop")

list_dir = os.listdir()

def remove_empty_dirs(list_dir):
    for _dir in list_dir:
        dir_path = os.path.join(os.getcwd(), _dir)
        if os.path.isdir(dir_path):
            if len(os.listdir(dir_path)) == 0:
                print(dir_path)
                os.removedirs(dir_path)
                





                
