


def is_number(data) -> bool:
    """
    Checks if the data sent
    is of a numeric type.
    """
    if(not type(data) == int
    and not type(data) == float): 
        return False
    return True