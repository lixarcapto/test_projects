


from .valid_string import*
from .divide_string import*

"""
    Funcion que sirve para añadir un string 
    antes de la pocision indicada en el 
    string enviado.
"""
def insert_string(index:int, base_string:str, 
        new_string:str) -> str:
    r = ""
    valid_string(base_string, 2, True)
    valid_string(new_string, 0, True)
    array = divide_string(index, 
                base_string)
    r = array[0] + new_string + array[1]
    return r