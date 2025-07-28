


def is_index(INDEX:int, ARRAY:list)\
        -> bool:
    """
    TESTED
    Function that returns true if 
    the index argument sent is a 
    correct index for the array sent.
    """
    if(not isinstance(INDEX, int)):
        return False
    if(INDEX < 0): return False
    if(INDEX >= len(ARRAY)): return False
    return True