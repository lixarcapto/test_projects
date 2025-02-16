

from ....btpy_validator.mod.valid_string.valid_string import*


def divide_string(index:int, string:str)\
        -> list[str]:
    """
    Funcion que divide un string en el
    indice indicado.
    """
    #
    if(index < 0): index = 0
    if(index >= len(string)):
        raise Exception("out of range index")
    valid_string(string, 2)
    char = ""
    for i in range(index):
        char = string[i:i +1:1]
    array = string.split(char, 1)
    array[0] += char
    return array