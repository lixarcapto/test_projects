
from .valid_string import*

"""
    Funcion que corta el string enviado 
    despues de cierto string indicado 
    returnando la primera parte del string.
"""
def cut_from(string: str, caracter: str)\
    -> str:
    valid_string(string, 2, True)
    r_string = ""
    if caracter not in string: 
        return ""
    else:
        r_string += caracter
        r_string += string.split(caracter)[1]
        return r_string