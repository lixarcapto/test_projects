
from ..dict_number_are_equal.dict_number_are_equal import*

def identify_dict_number(
        NESTED_DICT:dict[dict], 
        DICT_NEW:dict[str, int])->str:
    """
    Funcion que identifica la clave de
    un diccionario numerico que sea igual
    al diccionario numerico enviado.
    Ignora los valores 0.
    """
    dict_ = {}
    is_equal = False
    for k in NESTED_DICT:
        dict_ = NESTED_DICT[k]
        is_equal = dict_number_are_equal(
             DICT_NEW,
            dict_
        )
        if(is_equal): return k
    return ""