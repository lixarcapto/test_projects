



def is_error_return(ANY_DATA:any)->bool:
    """
    TESTED
    Function that tests whether a value
    is a return error such as 
    none, void string, void dict void
    array, or void tuple
    """
    #
    if ANY_DATA == None: return True
    if ANY_DATA == "": return True
    if ANY_DATA == []: return True
    if ANY_DATA == {}: return True
    if ANY_DATA == (): return True
    return False