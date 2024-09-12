


def has_none(array:list, function)->bool:
    """
    Función que itera sobre los 
    elementos del array enviado 
    buscando si ninguno de los 
    elementos del array retornan 
    true a la función enviada.
    """
    for e in array:
        if(function(e)):
            return False
    return True