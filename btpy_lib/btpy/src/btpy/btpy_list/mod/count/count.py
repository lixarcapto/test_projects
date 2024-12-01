


def count(STRUCTURE:list|dict, CHECKER)\
        -> int:
    """
    Funcion que cuenta el numero de 
    verificaciones con una funcion 
    checker enviada.
    """
    n = 0
    array = []
    if(type(STRUCTURE) == dict):
        array = STRUCTURE.values()
    else:
        array = STRUCTURE
    for e in array:
        if(CHECKER(e)):
            n += 1
    return n