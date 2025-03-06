



def in_range(NUMBER: int|float, 
        RANGE_ARR_X2: list[int])\
        -> bool:
    """
    TESTED
    Function to identify if the input 
    number is contained within the 
    sending range. The range sent is 
    an integer array where index 0 
    is min and 1 is max.
    """
    # if range is not a list
    if(not type(RANGE_ARR_X2) == list):
        raise Exception(f"<!>Error: RANGE_ARR is not a range array ({NUMBER})")
    # if range does not have the 
    # required size
    if(not len(RANGE_ARR_X2) == 2):
        raise Exception(f"<!>Error: RANGE_ARR is not a range array ({NUMBER})")
    # is not a number
    if(not type(NUMBER) == int
    and not type(NUMBER) == float):
        raise Exception(f"<!>Error: NUMBER is not a number ({NUMBER})")
    for i in range(2):
        if(not type(RANGE_ARR_X2[i]) == int
        and not type(RANGE_ARR_X2[i]) == float):
            raise Exception(f"<!>Error: elements of RANGE_ARR_X2 are not a number ({RANGE_ARR_X2})")
    if(NUMBER >= RANGE_ARR_X2[0]
    and NUMBER <= RANGE_ARR_X2[1]):
        return True
    return False
