

def is_range(RANGE_ARRAY:list[int]):
    """
    Función que devuelve True si los 
    datos enviados son de tipo array 
    de rango.
    """
    # Si no es un array de longitud 2
    if (not isinstance(RANGE_ARRAY, list)) \
    or (len(RANGE_ARRAY) != 2):
        return False
    # Si no es un número
    if ((not isinstance(
            RANGE_ARRAY[0], 
            (int, float)
        )) 
    and (isinstance(
            RANGE_ARRAY[1], 
            (int, float)
        ))):
        return False
    # Si no es min y max
    if (not RANGE_ARRAY[0] 
            < RANGE_ARRAY[1]):
        return False
    return True