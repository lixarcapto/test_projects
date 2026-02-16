

from ..contains_dict.contains_dict import*

def witch_dict_contains_it(
        nested_dict:dict[str, dict], 
        content:dict[str, int])->str:
    """
    Funcion que identifica que diccionario
    de un diccionario anidado contiene 
    un diccionario numerico
    """
    dict_ = {}
    for k in nested_dict:
        dict_ = nested_dict[k]
        if(contains_dict(dict_, content)):
            return k
    return ""