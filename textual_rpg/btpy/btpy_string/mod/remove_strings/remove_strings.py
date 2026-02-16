


def remove_strings(STRING_PRIMAL:str,
        TO_REMOVE_LIST:list[str])->str:
    to_remove_list = []
    if(type(TO_REMOVE_LIST) == str):
        to_remove_list = list(TO_REMOVE_LIST)
    else: 
        to_remove_list = TO_REMOVE_LIST
    r_string = STRING_PRIMAL
    for string_to_remove in to_remove_list:
        r_string = r_string.replace(
            string_to_remove, "")
    return r_string