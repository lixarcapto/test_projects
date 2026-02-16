



def is_byte_127(ANY_DATA : any)\
        -> bool:
    """
    TESTED
    Function that returns true if 
    the data sent is a byte 127 type, 
    that is, an 8-bit integer between 
    the range -127 and 127.
    """
    if(not type(ANY_DATA) == int): return False
    if(ANY_DATA >= 127): return False
    if(ANY_DATA <= -127): return False
    return True