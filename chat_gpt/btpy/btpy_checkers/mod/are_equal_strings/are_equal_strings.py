


def are_equal_strings(STRING_1:str, 
        STRING_2:str)-> bool:
    """
    Function that checks if two 
    strings are equal, ignoring case.
    TESTED
    """
    if(not isinstance(STRING_1, str)):
        raise Exception(f"The parameter STRING_1 is not a string, its value is \"{STRING_1}\" and its type is {type(STRING_1)}.")
    if(not isinstance(STRING_2, str)):
        raise Exception(f"The parameter STRING_2 is not a string, its value is \"{STRING_2}\" and its type is {type(STRING_2)}.")
    return STRING_1.lower() \
        == STRING_2.lower()