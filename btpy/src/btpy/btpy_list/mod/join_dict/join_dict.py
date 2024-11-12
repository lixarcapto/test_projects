



def join_dict(DICT_A:dict, 
        DICT_B:dict)->dict:
    """
    function that combines two 
    dictionaries into one.
    """
    result_dict = DICT_A
    result_dict |= DICT_B
    return result_dict