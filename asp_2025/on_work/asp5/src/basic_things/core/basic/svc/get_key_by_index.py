

"""
    Funcion que busca la key de un diccionario
    por un indice numerico.
"""
#
def get_key_by_index(map, index):
    i = 0
    for key in map:
        if(index == i):
            return key
        i += 1
    return ""
