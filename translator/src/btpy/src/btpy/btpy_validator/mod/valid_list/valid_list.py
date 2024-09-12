


from ....btpy_utilitys.mod.deep.deep import*


def valid_list(array:list, 
        deep_int:int = -1) ->None:
    """
    Función que valida una lista 
    enviada si es lista, si no es 
    void y si tiene la profundidad 
    indicada[opcional]
    """
    # valid the parameter array
    if(not type(array) == list): 
        txt = f"array parameter is not array "
        txt += "type {array}"
        raise Exception(txt)
    if(array == []):
        txt = "array parameter is void"
        raise Exception(txt)
    if(not deep(array) == deep_int
    and not deep == -1):
        txt = f"array parameter is not x{deep_int}"
        raise Exception(txt)