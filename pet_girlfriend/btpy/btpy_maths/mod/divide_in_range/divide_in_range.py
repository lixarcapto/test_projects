


def divide_in_range(
        DIVIDEND:list[int|float], 
        DIVIDER:list[int|float],
        RANGE_LIST:list[int|float])\
        ->int|float:
    """
    function that divides two 
    numbers keeping the result in 
    the given range.
    """
    result = DIVIDEND / DIVIDER
    if(result >= RANGE_LIST[1]):
        return RANGE_LIST[1]
    if(result <= RANGE_LIST[0]):
        return RANGE_LIST[0]
    return result