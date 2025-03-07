


from ..is_byte_256.is_byte_256 import*

def is_RGBA(ANY_DATA:any)->bool:
    """
    Function that returns true if 
    the data sent is an RGBA array; 
    that is, an x4 array where the 
    first 3 elements are integers of 
    range 256 that represent the 
    colors red, green and blue; and 
    the last element (index 3) is 
    the alpha value which is a float 
    of range 0 and 1.
    """
    # if is not a lista
    if((not type(ANY_DATA) == list)
    and (not type(ANY_DATA) == tuple)): 
        return False
    # if the list does not have the 
    # size x4
    if(not len(ANY_DATA) == 4): 
        return False
    # if RGB values ​​are not integer 256
    if(not is_byte_256(ANY_DATA[0])): 
        return False
    if(not is_byte_256(ANY_DATA[1])): 
        return False
    if(not is_byte_256(ANY_DATA[2])): 
        return False
    # if the alpha value is not in 
    # the range 0 and 1
    if(not ANY_DATA[3] >= 0): return False
    if(not ANY_DATA[3] <= 1): return False 
    return True