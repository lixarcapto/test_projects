


def count_true_checks(STRUCTURE:list|dict,
        CHECKER_FUNCTION)-> int:
    """
    Funcion que cuenta el numero de 
    verificaciones al recorrer una
    estructura. Funciona aplicando a 
    cada elemento de la estructura 
    la funcion checker enviada y contando 
    los resultados verdaderos.
    """
    n:int = 0
    array:list = []
    type_:str = type(STRUCTURE)
    # si no es una funcion checker
    if(not type(CHECKER_FUNCTION(1)) 
            == bool):
        raise Exception(f"<!>Error: CHECKER_FUNCTION must be a checker function type, for example (lambda e:e > 1)")
    # si no es diccionario o una lista
    if((not type_ == dict)
    and (not type_ == list)):
        raise Exception(f"<!>Error: STRUCTURE is not a valid data type is ({type_}), it must be dict or list")
    if(type_ == dict):
        array = STRUCTURE.values()
    else:
        array = STRUCTURE
    for e in array:
        if(CHECKER_FUNCTION(e)):
            n += 1
    return n