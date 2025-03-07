


def is_number(ANY_DATA:any) -> bool:
    """
    TESTED
    Function that returns true if 
    the data sent is of float or 
    integer type.
    """
    if(not type(ANY_DATA) == int
    and not type(ANY_DATA) == float): 
        return False
    return True