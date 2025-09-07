


def write_dict(DICT:str)->str:
    """
    Funcion que escribe de forma
    ordenada un diccionario de una
    dimension.
    """
    txt = "{\n"
    n = 0
    max_ = len(DICT)
    margin_size = 2
    margin = " " * margin_size
    for k in DICT:
        txt += f"{margin}\"{k}\" : {DICT[k]}"
        if(n < max_ -1):
            txt += ","
        txt += "\n"
        n += 1
    txt += "}\n"
    return txt