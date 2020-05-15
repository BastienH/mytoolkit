import os
import glob

"""
source : https://stackoverflow.com/questions/39327032/how-to-get-the-latest-file-in-a-folder-using-python
"""
def get_latest_file_in_dir(path):
    listdir = glob.glob(f"{path}/*")
    latest_file = max(listdir, key=os.path.getctime)
    return latest_file
    
