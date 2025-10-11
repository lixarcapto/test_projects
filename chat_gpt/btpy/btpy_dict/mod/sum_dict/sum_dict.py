


def sum_dict(DICT_1:dict[str, int],
             DICT_2:dict[str, int])->dict:
    """
    Funcion que permite sumar dos 
    diccionarios de numeros.
    """
    DICT_R:dict[str, int] = {}
    for k in DICT_1:
        DICT_R[k] = DICT_1[k]
    for k in DICT_2:
        if(k in DICT_R):
            DICT_R[k] += DICT_2[k]
        else:
            DICT_R[k] = DICT_2[k]
    return DICT_R