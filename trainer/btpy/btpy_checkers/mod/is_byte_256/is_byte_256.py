



def is_byte_256(ANY : any)-> bool:
    """
     función que verifica si el dato 
     enviado es un tipo byte 256
    """
    if(not type(ANY) == int): return False
    if(ANY >= 256): return False
    if(ANY < 0): return False
    return True