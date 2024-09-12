


def has_all(array:list, function):
    """
    Función que itera sobre los elementos del
    array enviado buscando si todos los 
    elementos del array retornan true a la 
    función enviada.
    """
    for e in array:
        if(not function(e)):
            return False
    return True