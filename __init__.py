from .file_num_increment import *
from .replace_last import *
from .read import *
from .get_latest_file_in_dir import *

__doc__ = """
A set of functions for scripts
"""

"""
To do : import automatically functions from files in the current package

import os

cwd = os.getcwd()

for file in os.listdir(cwd):
	from .{os.path.basename(file)} import *
	
"""
