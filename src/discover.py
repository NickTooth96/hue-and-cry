import os 
import threading
import time


def get_list_as_dictionary_recursive(src=os.getcwd()):
    """returns list of all files in directory

    Args:
        src (_type_): _description_

    Returns:
        dict: dictionary of all files in current directory (src)
    """    
    if src != os.getcwd():
        src = os.path.join('',src)
    out =  {i:os.path.join(src,i) for i in os.listdir(src)}
    return {k: get_list_as_dictionary_recursive(v) if os.path.isdir(v) else v for k,v in out.items()} 

def get_list_as_dictionary(src=os.getcwd()):
    """returns list of all files in directory

    Args:
        src (_type_): _description_

    Returns:
        dict: dictionary of all files in current directory (src)
    """    
    if src != os.getcwd():
        src = os.path.join('',src)
    out =  {i:os.path.join(src,i) for i in os.listdir(src)}
    ## change  so that the value is True if it is a directory and the key as the full path
    return {v: True if os.path.isdir(v) else v for k,v in out.items()}

def recursive_list(src=os.getcwd()):
    """returns list of all files in directory and subdirectories

    Args:
        src (_type_): _description_

    Returns:
        list: list of all files in current directory (dest)
    """
    buffer = []
    output = []
    if src != os.getcwd():
        src = os.path.join('',src)
    for root, dirs, files in os.walk(src):
        for file in files:
            buffer.append(file)
    return buffer

def hue(key,search_path=os.path.expanduser('~')):
    start_time = time.time()
    results = cry(key,search_path)   
    run_time = time.time() - start_time
    print(f'--- Execution Time: {run_time:.2f} ---')  
    return results

def _cry(key,search_path):

    results = {}

    for subdir, dirs, files in os.walk(search_path):
        for file in files:
            if os.path.isfile(os.path.join(subdir, file)):                
                if key in file:            
                    print(f'Found: {clickable_link("file://wsl.localhost/Ubuntu" + os.path.join(subdir,file))}')
                    results[file] = os.path.join(subdir, file)
    return results

def cry(key, element):
    if key in element:
        return True
    else:
        return False

def clickable_link(url, text=None):
    if text is None:
        text = url
    return f"\033]8;;{url}\033\\{text}\033]8;;\033\\"

def multi_hue(key, search_path):
    dirlist = get_list_as_dictionary(search_path)
    print(dirlist)

def threads(key, search_path, thread_num=1, output={}):
    dir_list = os.listdir(search_path)
    for element in dir_list:
        element = os.path.join(search_path, element)
       
        if os.path.isdir(element):
            # print(f"Thread {thread_num} is searching {element} for {key}")
            t = threading.Thread(target=threads, args=(key,element, thread_num+1, output))
            t.start()
            t.join()
        else:
            if cry(key, element):
                print(f"Found {key} in {search_path}")
                score = string_hamming_distance(key, element.split('/')[-1])
                output[score] = os.path.join(search_path, element) 
            else:
                pass
    output = dict(sorted(output.items()))
    return output

def string_hamming_distance(s1, s2):
    s1 = s1.strip().lower()
    s2 = s2.strip().lower()
    distance = 0
    if len(s1) != len(s2):
        distance += abs(len(s1) - len(s2))
    for i in range(min(len(s1), len(s2))):
        if s1[i] != s2[i]:
            distance += 1
    return distance