

def is_range(RANGE_ARRAY_X2
        :list[int|float])\
        -> bool:
    """
    Function that returns true if the 
    data sent is a range in array 
    format, that is, an array of int 
    or float of size x2 where index 0 
    is min and index 1 is max; if the 
    data is not a range, it will return 
    false.
    """
    # Si no es un array de longitud 2
    if (not isinstance(RANGE_ARRAY_X2, list)) \
    or (len(RANGE_ARRAY_X2) != 2):
        return False
    # Si no es un número
    if ((not isinstance(
            RANGE_ARRAY_X2[0], 
            (int, float)
        )) 
    and (isinstance(
            RANGE_ARRAY_X2[1], 
            (int, float)
        ))):
        return False
    # Si no es min y max
    if (not RANGE_ARRAY_X2[0] 
            < RANGE_ARRAY_X2[1]):
        return False
    return True