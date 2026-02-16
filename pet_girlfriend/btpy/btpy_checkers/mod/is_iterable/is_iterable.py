


def is_iterable(ANY_DATA:any)-> bool:
    """
    TESTED
    Function that returns true if
    the data sent is of an iterable type; 
    that is a list, set, dict, tuple, or 
    string type.
    """
    if((not isinstance(ANY_DATA, list))
    and (not isinstance(ANY_DATA, set))
    and (not isinstance(ANY_DATA, dict))
    and (not isinstance(ANY_DATA, str))
    and (not isinstance(ANY_DATA, tuple))):
        return False
    return True