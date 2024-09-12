


def map_in_keys(OLD_DICT:dict, function)\
        ->dict:
    new_dict = {}
    for k in OLD_DICT:
        new_dict[function(k)] = OLD_DICT[k]
    return new_dict