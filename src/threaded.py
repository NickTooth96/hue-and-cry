import os 
import sys
import threading
import datetime

def hue(key,search_path=os.path.expanduser('~'), thread_count=1, possible_matches=[]):
    """List all files in a directory. If file calls cry if directory calls hue"""
    
    files = []
    directories = []

    # list files in search_path
    for file in os.listdir(search_path):
        file_path = os.path.join(search_path,file)
        if os.path.isfile(file_path):
            # print(f"Thread {thread_count} checking: {file}")
            t = threading.Thread(target=cry, args=(key,file_path, possible_matches))
            t.start()
            t.join()
        else:
            if file[0] != '.':
                # print(f"Thread {thread_count} looking in: {directory}")
                t = threading.Thread(target=hue, args=(key,file_path, thread_count + 1, possible_matches))
                t.start()
                t.join()       

    return possible_matches

def cry(key, file, potential_files):
    if key in file:
        # print(f"Found: {file}")
        potential_files.append(file)
    return potential_files

def check_first():
    print("Check first")
    return True



start_time = datetime.datetime.now()
test = hue(sys.argv[1])
for t in test:
    print(t)
print("Time taken:",datetime.datetime.now()-start_time)