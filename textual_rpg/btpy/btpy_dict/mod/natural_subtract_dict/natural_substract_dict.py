


def natural_substract_dict(MINUEND:dict, 
        SUBTRANDH:dict)->dict:
    """
    Funcion que resta un diccinario
    de numeros a otro diccionario de
    numeros.
    """
    DICT_R = {}
    r = 0
    for k in MINUEND:
        DICT_R[k] = MINUEND[k]
    for k in SUBTRANDH:
        if(k in DICT_R):
            DICT_R[k] -= SUBTRANDH[k]
            if(DICT_R[k] < 0):
                DICT_R[k] = 0
    return DICT_R
