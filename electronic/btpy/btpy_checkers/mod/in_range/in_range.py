


from ..is_range.is_range import*

def in_range(NUMBER: int|float, 
        RANGE_LIST_X2: list[int|float])\
        -> bool:
    """
    Function to identify if the input 
    number is contained within the 
    sending range. The range sent is 
    an integer array where index 0 
    is min and 1 is max.
    FINAL
    """
    # VALITATORS ------------------------
    # if range is not a list
    if(not is_range(RANGE_LIST_X2)):
        raise Exception(f"RANGE_ARR parameter is not a range array ({RANGE_LIST_X2})")
    if(not type(NUMBER) == int
    and not type(NUMBER) == float):
        raise Exception(f"NUMBER parameter is not a number ({NUMBER})")
    # FUNCTIONALITY --------------------------
    if(NUMBER >= RANGE_LIST_X2[0]
    and NUMBER <= RANGE_LIST_X2[1]):
        return True
    # If it does not detect any errors 
    # in the parameters, it returns true.
    return False
