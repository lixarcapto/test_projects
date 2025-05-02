

from .valid_string import*

def cut_until(string: str, caracter: str)\
    -> str:
    valid_string(string, 2, True)
    r_string = ""
    if caracter not in string: 
        return ""
    else:
        r_string = string.split(caracter)[0]
        r_string += caracter
        return r_string