



def is_error(value)->bool:
    """
    Function that tests whether a value
    is a return error such as -1,
    none, void string, void dict, or void
    array
    """
    #
    if value == -1: return True
    if value == None: return True
    if value == "": return True
    if value == []: return True
    if value == {}: return True
    if value == (): return True
    return False