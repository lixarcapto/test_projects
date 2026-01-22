



def is_ordered_iterable(ANY_DATA:any)\
        -> bool:
    """
    Function that returns true if 
    the data sent is an ordered iterable 
    type such as list, tuple, and string.
    """
    if(isinstance(ANY_DATA, list)):
        return True
    if(isinstance(ANY_DATA, tuple)):
        return True
    if(isinstance(ANY_DATA, str)):
        return True
    return False