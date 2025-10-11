

def dict_number_are_equal(
          DICT_1:dict[str, int], 
          DICT_2:dict[str, int])->bool:
    """
    Funcion que identifica si dos 
    diccionarios numericos son iguales
    ignorando los valores 0.
    """
    clean_1 = clean_dict_number(DICT_1)
    clean_2 = clean_dict_number(DICT_2)
    return clean_1 == clean_2

def clean_dict_number(DICT:dict)->dict:
    dict_ = {}
    for k in DICT:
        if(DICT[k] == 0): continue
        dict_[k] = DICT[k]
    return dict_