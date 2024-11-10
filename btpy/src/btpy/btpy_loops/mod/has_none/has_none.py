


def has_none(array:list|dict|str, function)->bool:
    """
    Función que itera sobre los 
    elementos del array enviado 
    buscando si ninguno de los 
    elementos del array retornan 
    true a la función enviada.
    """
    data = None
    if(type(array) == dict):
        data = array.values()
    else:
        data = array
    for e in data:
        if(function(e)):
            return False
    return True