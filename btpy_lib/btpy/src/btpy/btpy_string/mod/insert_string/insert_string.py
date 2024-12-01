


from ....btpy_validator.mod.valid_string import*
from ...mod.divide_string.divide_string import*


def insert_string(index:int, 
        base_string:str, 
        new_string:str) -> str:
    """
    Funcion que sirve para añadir 
    un string  antes de la pocision 
    indicada en el string enviado.
    """
    #
    r = ""
    valid_string(base_string, 2, True)
    valid_string(new_string, 0, True)
    array = divide_string(index, 
                base_string)
    r = array[0] + new_string + array[1]
    return r