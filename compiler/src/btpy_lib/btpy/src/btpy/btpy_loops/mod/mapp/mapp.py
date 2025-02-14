



def mapp(DATA:list|dict|str, FUNCTION)\
        -> list|dict|str:
    """
    Function that improves the map 
    function to support dict, list and str.
    """
    # in case of list
    if(isinstance(DATA, list)):
        return list(map(FUNCTION, DATA))
    result = None
    # in case of dict
    if(isinstance(DATA, dict)):
        result = {}
        for k in DATA:
            result[k] = FUNCTION(DATA[k])
        return result
    # in case of string
    if(isinstance(DATA, str)):
        result = ""
        for char in DATA:
            result += FUNCTION(char)
        return result
    raise Exception(
        "Error:data is not list, dict or str")