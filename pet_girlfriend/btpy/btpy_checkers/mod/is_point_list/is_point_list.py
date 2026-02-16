

from ..is_point.is_point import*

def is_point_list_2D(ANY_DATA : any)-> bool:
    """
    Function that returns true if 
    the data sent is a pont list 
    in the format of an array of 
    numbers of size x2; and returns 
    false if it is not.
    """
    if(not isinstance(ANY_DATA, list)):
        return False
    for e in ANY_DATA:
        if(not is_point_2D(e)):
            return False
    return True

def is_point_list_3D(ANY_DATA : any)-> bool:
    """
    Function that returns true if 
    the data sent is a pont list 
    in the format of an array of 
    numbers of size x3; and returns 
    false if it is not.
    """
    if(not isinstance(ANY_DATA, list)):
        return False
    for e in ANY_DATA:
        if(not is_point_3D(e)):
            return False
    return True