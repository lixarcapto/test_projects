

def is_range(ANY_DATA:any)-> bool:
    """
    Function that returns true if the 
    data sent is a range in array 
    format, that is, an array of int 
    or float of size x2 where index 0 
    is min and index 1 is max; if the 
    data is not a range, it will return 
    false.
    FINAL
    """
    # Si no es un array de longitud 2
    if (not isinstance(ANY_DATA, list)) \
    or (len(ANY_DATA) != 2):
        return False
    # Si no es un número
    if ((not isinstance(
            ANY_DATA[0], 
            (int, float)
        )) 
    and (isinstance(
            ANY_DATA[1], 
            (int, float)
        ))):
        return False
    # Si no es min y max
    if (not ANY_DATA[0] 
            < ANY_DATA[1]):
        return False
    return True