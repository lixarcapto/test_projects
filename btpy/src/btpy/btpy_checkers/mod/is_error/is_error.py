



def is_error(value)->bool:
    """
    Function that tests whether a value
    is a return error such as 
    none, void string, void dict, or void
    array
    """
    #
    if value == None: return True
    if value == "": return True
    if value == []: return True
    if value == {}: return True
    if value == (): return True
    return False