


def has_some(array:list|dict|str, function)->bool:
    """
    Función que itera sobre los 
    elementos del array enviado 
    buscando si alguno de los 
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
            return True
    return False