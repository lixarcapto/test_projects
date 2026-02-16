


def multiply_in_range(
        MULTIPLYING:int|float,
        MULTIPLIER:int|float,
        RANGE_LIST:list[int|float])\
        ->int|float:
    """
    function that multiplies two numbers 
    keeping the result of the 
    multiplication in the given range.
    """
    result:int|float = MULTIPLYING\
        * MULTIPLIER
    if(result >= RANGE_LIST[1]):
        return RANGE_LIST[1]
    if(result <= RANGE_LIST[0]):
        return RANGE_LIST[0]
    return result