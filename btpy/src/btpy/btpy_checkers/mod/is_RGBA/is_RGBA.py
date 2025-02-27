


def is_RGBA(ANY:any)->bool:
    """
    Checker que verifica si un 
    dato es de tipo rgba lista o tupla
    """
    if((not type(ANY) == list)
    and (not type(ANY) == tuple)): 
        return False
    if(not len(ANY) == 4): return False
    if(not __is_byte256(ANY[0])): 
        return False
    if(not __is_byte256(ANY[1])): 
        return False
    if(not __is_byte256(ANY[2])): 
        return False
    if(not ANY[3] >= 0): return False
    if(not ANY[3] <= 1): return False 
    return True

def __is_byte256(data)\
        -> bool:
    """
     función que verifica si el dato 
     enviado es un tipo byte 256
    """
    if(not type(data) == int): return False
    if(data >= 256): return False
    if(data < 0): return False
    return True