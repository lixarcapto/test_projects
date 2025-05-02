

from .is_byte import*

def is_rgb(data):
    if(not type(data) == list): return False
    if(len(data) > 3): return False
    for e in data:
        if(not is_byte(e)): return False
    return True
