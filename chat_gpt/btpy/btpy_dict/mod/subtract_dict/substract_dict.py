


def substract_dict(MINUEND:dict, 
        SUBTRANDH:dict)->dict:
    """
    Funcion que resta un diccinario
    de numeros a otro diccionario de
    numeros.
    """
    DICT_R = {}
    for k in MINUEND:
        DICT_R[k] = MINUEND[k]
    for k in SUBTRANDH:
        if(k in DICT_R):
            DICT_R[k] -= SUBTRANDH[k]
        else:
            DICT_R[k] = SUBTRANDH[k] * -1
    return DICT_R
