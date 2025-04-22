


def is_number(ANY_DATA:any) -> bool:
    """
    Function that returns true if 
    the data sent is float or 
    integer type.
    FINAL
    """
    if(not type(ANY_DATA) == int
    and not type(ANY_DATA) == float): 
        return False
    return True