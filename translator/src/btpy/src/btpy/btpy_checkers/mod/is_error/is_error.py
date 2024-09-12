



def is_error(value)->bool:
    """
    Funcion que analiza si un valor 
    es un error de retorno como  -1, 
    none, void string, void dict o void array
    """
    #
    if value == -1: return True
    if value == None: return True
    if value == "": return True
    if value == []: return True
    if value == {}: return True
    return False