


from ..find_value.find_value import*

def find_closest_lower(DICT:dict, 
        NUMBER:int|float):
    """
    funcion que identifica en un 
    diccionario de numeros que numero 
    es el mas cercano inferior al numero 
    enviado; retornando su clave.
    """
    values_arr = sorted(DICT.values())
    former_number:int|float = 0
    for value in values_arr:
        if(value > NUMBER):
            break
        former_number = value
    key = find_value(DICT, former_number)
    return key