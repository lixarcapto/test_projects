



def find_value(DICT:dict, VALUE)->str:
    """
    Busca la clave del valor enviado
    en el diccionario.
    """
    for k in DICT:
        if(VALUE == DICT[k]):
            return k
    return ""