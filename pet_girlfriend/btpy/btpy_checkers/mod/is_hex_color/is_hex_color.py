


import re

def is_hex_color(ANY_DATA : any)\
        -> bool:
    """
    TESTED
    Function that returns true if 
    the data sent is a hexadecimal 
    color code string (hex color) and 
    returns false if it is not.
    """
    if (not isinstance(ANY_DATA, str)):
        return False
    patron = r'^#([0-9A-Fa-f]{3}){1,2}$'
    return bool(re.match(patron, ANY_DATA))