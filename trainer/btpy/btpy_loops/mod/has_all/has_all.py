


def has_all(ARRAY:list|dict|str, function):
    """
    Función que itera sobre los elementos del
    array enviado buscando si todos los 
    elementos del array retornan true a la 
    función enviada.
    """
    data = None
    if(type(ARRAY) == dict):
        data = ARRAY.values()
    else:
        data = ARRAY
    for e in data:
        if(not function(e)):
            return False
    return True