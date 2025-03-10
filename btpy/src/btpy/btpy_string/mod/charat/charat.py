



def charat(STRING:str, INDEX:int) -> str:
    """
    # return char
    Funcion que extrae una letra 
    del string en un index 
    especifico usando slicing.
    """
    # valid index
    if(not type(INDEX) == int):
        raise Exception("index is not int")
    # funcion
    if(not INDEX < len(STRING)):
        txt = f"string out of range "
        txt += "index {index} of leng "
        txt += "{len(string)}"
        raise Exception(txt)
    return STRING[INDEX:INDEX + 1]