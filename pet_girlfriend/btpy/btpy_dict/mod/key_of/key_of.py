



def key_of(DICT:dict, VALUE:any)->str:
    """
    TESTED
    Function that searches for the 
    key associated with the value 
    sent in the dictionary.
    """
    if(not isinstance(DICT, dict)):
        raise Exception("The DICT parameter is not a dict type.")
    for k in DICT:
        if(VALUE == DICT[k]):
            return k
    raise Exception("The dictionary sent in the DICT parameter does not have the value sent in the VALUE parameter.")