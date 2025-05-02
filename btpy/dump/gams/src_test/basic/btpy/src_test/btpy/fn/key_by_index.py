


"""
    Funcion que busca la key de un diccionario
    por un indice numerico.
"""
def key_by_index(dict, index: int) -> str:
    i = 0
    for key in dict:
        if(index == i):
            return key
        i += 1
    return ""