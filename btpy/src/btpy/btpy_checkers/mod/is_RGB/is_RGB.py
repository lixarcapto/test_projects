



def is_RGB(ANY : any)->bool:
    """
    TESTED
    Checker que verifica si un 
    dato es de tipo rgb lista
    """
    if(not type(ANY) == list): return False
    if(not len(ANY) == 3): return False
    for e in ANY:
        if(not __is_byte_256(e)): 
            return False
    return True

def __is_byte_256(ANY : any)-> bool:
    """
     función que verifica si el dato 
     enviado es un tipo byte 256
    """
    if(not type(ANY) == int): return False
    if(ANY >= 256): return False
    if(ANY < 0): return False
    return True
