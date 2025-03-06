



def in_range(NUMBER: int, RANGE_ARR: list)\
        -> bool:
    """
    TESTED
    Function to identify if the input 
    number is contained within the 
    sending range.
    """
    # if range is not a list
    if(not type(RANGE_ARR) == list):
        raise Exception(f"<!>Error: RANGE_ARR is not a range array ({NUMBER})")
    # if range does not have the 
    # required size
    if(not len(RANGE_ARR) == 2):
        raise Exception(f"<!>Error: RANGE_ARR is not a range array ({NUMBER})")
    # is not a number
    if(not type(NUMBER) == int
    and not type(NUMBER) == float):
        raise Exception(f"<!>Error: NUMBER is not a number ({NUMBER})")
    if(NUMBER >= RANGE_ARR[0]
    and NUMBER <= RANGE_ARR[1]):
        return True
    return False
