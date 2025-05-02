


"""
    Funcion que analiza la profundidad de un 
    array retornando su nivel de profundidad 
    como un int, si no es array retornara 0.
    TODO: Mejorar para que analize tambien 
    diccionarios.
"""
def deep(array:list) -> int:
    level = 0
    if(type(array) == type([])):
        level = 1
        level = __calcule_deep(array, level)
    return level

def __calcule_deep(array, level):
    for i in range(len(array)):
        if(type(array[i]) == type([])):
            level += 1
            level = __calcule_deep(array[i], level)
            break
    return level
