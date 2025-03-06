


def map_in_keys(OLD_DICT:dict, FUNCTION)\
        ->dict:
    """
    function that goes through all the 
    keys in a dictionary by applying 
    the sent function.
    """
    new_dict = {}
    for k in OLD_DICT:
        new_dict[FUNCTION(k)] = OLD_DICT[k]
    return new_dict