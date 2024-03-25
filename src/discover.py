import os 
import time


def get_list(src=os.getcwd()):
    """returns list of all files in directory

    Args:
        src (_type_): _description_

    Returns:
        list: list of all files in current directory (dest)
    """
    buffer = []
    output = []
    if src != os.getcwd():
        src = os.path.join('',src)
    return os.listdir(src)

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

def cry(key,search_path):

    results = {}

    for subdir, dirs, files in os.walk(search_path):
        for file in files:
            if os.path.isfile(os.path.join(subdir, file)):                
                if key in file:            
                    print(f'Found: {clickable_link("file://wsl.localhost/Ubuntu" + os.path.join(subdir,file))}')
                    results[file] = os.path.join(subdir, file)
    return results

def clickable_link(url, text=None):
    if text is None:
        text = url
    return f"\033]8;;{url}\033\\{text}\033]8;;\033\\"