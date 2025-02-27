



def in_range(NUMBER: int, RANGE_ARR: list)\
        -> bool:
    """
    Function to identify if the input 
    number is contained within the 
    sending range.
    """
    if(not type(RANGE_ARR) == list):
        print(f"<!>Error: RANGE_ARR is not a range array ({NUMBER})")
        return False
    if(not len(RANGE_ARR) == 2):
        print(f"<!>Error: RANGE_ARR is not a range array ({NUMBER})")
        return False
    if(not type(NUMBER) == int
    and not type(NUMBER) == float):
        print(f"<!>Error: NUMBER is not a number ({NUMBER})")
        return False
    if(NUMBER >= RANGE_ARR[0]
    and NUMBER <= RANGE_ARR[1]):
        return True
    return False
