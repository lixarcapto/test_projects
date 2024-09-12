

from ..is_byte.is_byte import*


def is_rgb(data)->bool:
    """
    Checker que verifica si un 
    dato es de tipo rgb lista
    """
    if(not type(data) == list): return False
    if(not len(data) == 3): return False
    for e in data:
        if(not is_byte256(e)): return False
    return True

def is_rgba(data)->bool:
    """
    Checker que verifica si un 
    dato es de tipo rgba lista
    """
    if(not type(data) == list): return False
    if(not len(data) == 4): return False
    for e in data:
        if(not is_byte256(e)): return False
    return True
