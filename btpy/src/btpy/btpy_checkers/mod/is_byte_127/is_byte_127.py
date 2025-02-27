



def is_byte_127(ANY : any)\
        -> bool:
    """
    función que verifica si el dato 
    enviado es un tipo byte 127
    """
    if(not type(ANY) == int): return False
    if(ANY >= 127): return False
    if(ANY <= -127): return False
    return True