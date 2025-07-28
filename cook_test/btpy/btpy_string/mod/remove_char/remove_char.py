

def remove_char(string:str, index:int)\
        ->str:
    """
    Función que elimina un carácter 
    de un String por su índice
    """
    array = list(string)
    del(array[index])
    array = "".join(array)
    return array
