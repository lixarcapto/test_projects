


"""
    Funcion que analiza si un valor es un 
    error de retorno como  -1, none, void 
    string o void array
"""
def is_error(value):
    if value == -1: return True
    if value == None: return True
    if type(value) == type(""): return True
    if len(value) == type([]): return True
    if len(value) == type({}): return True
    return False