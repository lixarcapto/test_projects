

"""
Comprueba si el dato enviado el de un tipo 
numérico.
"""
def is_number(data) -> bool:
    if(not type(data) == int
    and not type(data) == float): 
        return False
    return True