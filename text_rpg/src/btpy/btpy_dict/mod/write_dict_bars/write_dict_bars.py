


def write_dict_bars(DICT:str, 
        BAR_SYMBOL:str = "/")->str:
    txt = ""
    # identifica la clave mas grande
    max_size = 0
    for k in DICT:
        if(len(k) > max_size):
            max_size = len(k)
    remaining = 0
    for k in DICT:
        remaining = max_size - len(k)
        txt += f"{k} " 
        txt += " " * remaining
        txt += str(DICT[k]) + " "
        txt += BAR_SYMBOL * DICT[k]
        txt += "\n"
    return txt
