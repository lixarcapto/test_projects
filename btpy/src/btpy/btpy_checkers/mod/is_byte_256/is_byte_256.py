



def is_byte_256(ANY_DATA : any)-> bool:
    """
    TESTED
    Function that returns true if 
    the data sent is a byte 256 type, 
    that is, an 8-bit integer in the 
    range between 0 and 256.
    """
    if(not type(ANY_DATA) == int): 
        return False
    if(ANY_DATA >= 256): return False
    if(ANY_DATA < 0): return False
    return True