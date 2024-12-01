


def is_byte256(data)\
        -> bool:
    """
     función que verifica si el dato 
     enviado es un tipo byte 256
    """
    if(not type(data) == int): return False
    if(data >= 256): return False
    if(data < 0): return False
    return True

def is_byte127(data)\
        -> bool:
    """
     función que verifica si el dato 
     enviado es un tipo byte 127
    """
    if(not type(data) == int): return False
    if(data >= 127): return False
    if(data <= -127): return False
    return True