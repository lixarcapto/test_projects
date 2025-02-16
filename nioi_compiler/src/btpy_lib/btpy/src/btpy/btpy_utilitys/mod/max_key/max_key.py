




def max_key(dict_of_numbers:dict)->str:
    """
    Calcula la clave mas alta en 
    un diccionario de numeros.
    """
    if(not is_dict_number(dict_of_numbers)):
        raise Exception(
        f"is not a dict ({dict_of_numbers})"
        )
    maximum = None
    for value in dict_of_numbers.values():
        if((maximum is None) 
        or (value > maximum)):
            maximum = value
    for k in dict_of_numbers:
        if(dict_of_numbers[k] == maximum):
            return k
    return ""

def min_key(dict_of_numbers:dict)->str:
    """
    Calcula la clave mas alta en 
    un diccionario de numeros.
    """
    if(not is_dict_number(dict_of_numbers)):
        raise Exception(
        f"is not a dict ({dict_of_numbers})"
        )
    minimum = None
    for value in dict_of_numbers.values():
        if((minimum is None) 
        or (value < minimum)):
            minimum = value
    for k in dict_of_numbers:
        if(dict_of_numbers[k] == minimum):
            return k
    return ""

def is_dict_number(data):
    if(not type(data) == dict):
        return False
    if(data == {}):
        return False
    for k in data:
        if(not type(data[k]) == int
        and not type(data[k]) == float):
            return False
    return True