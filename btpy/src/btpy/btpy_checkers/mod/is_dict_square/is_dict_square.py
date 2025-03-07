


from ...mod.is_number.is_number import is_number

def is_dict_square(ANY_DATA: any)-> bool:
    """
    Function that verifies if the 
    data sent is a rectangle in 
    dictionary format; this format 
    must contain the keys x for 
    location x, y for location y, 
    width for the size in x and height 
    for the size in y.
    """
    if(not isinstance(ANY_DATA, dict)):
        return False
    if(not "x" in ANY_DATA): return False
    if(not "y" in ANY_DATA): return False
    if(not "height" in ANY_DATA):
        return False
    if(not "width" in ANY_DATA):
        return False
    for k in ANY_DATA:
        if(not is_number(ANY_DATA[k])):
            return False
    return True
    
        
