


from ....btpy_validator\
    .mod.valid_string.valid_string import*



def charat(string:str, index:int) -> str:
    """
    # return char
    Funcion que extrae una letra 
    del string en un index 
    especifico usando slicing.
    """
    valid_string(string, 1)
    # valid index
    if(not type(index) == int):
        raise Exception("index is not int")
    # funcion
    if(not index < len(string)):
        txt = f"string out of range "
        txt += "index {index} of leng "
        txt += "{len(string)}"
        raise Exception(txt)
    return string[index:index + 1]