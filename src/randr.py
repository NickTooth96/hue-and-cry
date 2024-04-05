import datetime
import os
import sys


def drive_discovery_rec(path, files=[]):    
    start_run = datetime.datetime.now()
    
    for element in os.listdir(path):
        element_path = os.path.join(path, element)
        if os.path.isfile(element_path):
            files.append(element_path)
        elif os.path.isdir(element_path):
            try:
                drive_discovery_rec(element_path, files)
            except PermissionError:
                pass

    return files, datetime.datetime.now()-start_run

def drive_discovery_oswalk(path, files=[]):
    start_run = datetime.datetime.now()


    ## use os walk to list all files in a directory and its subdirectories
    for root, dirs, file_names in os.walk(path):
        for file in file_names:
            files.append(os.path.join(root, file))
        for dir in dirs:
            print( len( files ))
            drive_discovery_oswalk(os.path.join(root, dir), files)
    return files, datetime.datetime.now() - start_run




root_path = os.path.expanduser('~')

# oswalk = drive_discovery_oswalk(root_path)
# print(f"Oswalk: {oswalk[1]} Found {len(oswalk[0])} files") 
# for file in oswalk[0]:
#     print(file)  

rec = drive_discovery_rec(root_path)
print(f"Recursion: {rec[1]} Found {len(rec[0])} files")
# for file in rec[0]:
#     print(file)
 