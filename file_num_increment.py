import os
import re
from .replace_last import *


def file_num_increment(full_fpath):
        """Increment (counter) on duplicate files """
        while os.path.isfile(full_fpath) == True:
                
                fpath, fext = os.path.splitext(full_fpath) #['C:\Users\Desktop\file(1)', '.ext']

                if re.findall("[(]\d+[)]", fpath) != []: #Check if there is (x) in the path.
                        for counter in range(1000): #Loop 1000 times
                                if fpath.endswith(f"({counter})"): 
                                        fpath = replace_last(fpath, f"({counter})", f"({counter+1})") #Replace the last occurence of (counter) in the string.
                                        full_fpath = fpath + fext
                                        break
                                else: #here we pass for cases where (counter) is in the file/folder name itself. We skip them.
                                        continue
                else: #If there is no (counter), we create (1)
                        counter = 1
                        full_fpath = fpath + '(' + str(counter) + ')' + fext

        return full_fpath
