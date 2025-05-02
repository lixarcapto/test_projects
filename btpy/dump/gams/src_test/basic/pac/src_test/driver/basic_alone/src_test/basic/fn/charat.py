

from .valid_string import*

"""
    Funcion que extrae una letra del string en
    una posicion especifica usando slicing.
"""
# return char
def charat(string:str, index:int) -> str:
    valid_string(string, 0, True)
    if(not type(index) == int):
        raise Exception("index is not int")
    if(not index < len(string)):
        txt = f"string out of range "
        txt += "index {index} of leng "
        txt += "{len(string)}"
        raise Exception(txt)
    return string[index:index + 1]