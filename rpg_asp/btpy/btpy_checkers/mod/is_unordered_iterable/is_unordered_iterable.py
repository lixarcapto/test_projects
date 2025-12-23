

def is_unordered_iterable(ANY_DATA:any)\
        -> bool:
    """
    TESTED
    Function that returns true if 
    the data sent is an unordered iterable 
    type such as dict and set.
    """
    if(isinstance(ANY_DATA, dict)):
        return True
    if(isinstance(ANY_DATA, set)):
        return True
    return False