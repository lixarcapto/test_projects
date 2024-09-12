


def is_number(data) -> bool:
    """
    Comprueba si el dato enviado 
    es de un tipo numérico.
    """
    if(not type(data) == int
    and not type(data) == float): 
        return False
    return True