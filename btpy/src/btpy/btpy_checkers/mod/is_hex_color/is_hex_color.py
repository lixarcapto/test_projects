


import re

def is_hex_color(ANY : any):
    """
    TESTED
    Funcion que verifica si una cadena 
    es un color hexadecimal válido.
    """
    if (not isinstance(ANY, str)):
        return False
    # Expresión regular para verificar 
    # el formato hexadecimal
    patron = r'^#([0-9A-Fa-f]{3}){1,2}$'
    return bool(re.match(patron, ANY))