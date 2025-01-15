

def has_all_deep(DATA:list|dict|str, 
        FUNCTION)->bool:
    """
    Verifica si todos los elementos del 
    dato cumplen la condicion.
    """
    __valid_type(DATA)
    index = None
    for i, e in enumerate(DATA):
        # altera el index dependiendo si 
        # es un dict o list
        if(type(DATA) == dict):
            index = e
        else:
            index = i
        if(type(DATA[index]) == list 
        or type(DATA[index]) == dict):
            if(has_all_deep(DATA[index], 
                    FUNCTION)):
                return False
        if(not FUNCTION(DATA[index])):
            return False
    return True

def __valid_type(DATA)-> None:
    if((not type(DATA) == list)
    and (not type(DATA) == dict)
    and (not type(DATA) == str)):
        raise Exception(
        "Error:data is not a list, str or dict"
        )

def has_none_deep(DATA:list|dict, 
        FUNCTION)->bool:
    """
    Verifica si ninguno de los elementos 
    del dato cumplen la condicion.
    """
    __valid_type(DATA)
    index = None
    for i, e in enumerate(DATA):
        # altera el index dependiendo si 
        # es un dict o list
        if(type(DATA) == dict):
            index = e
        else:
            index = i
        if(type(DATA[index]) == list 
        or type(DATA[index]) == dict):
            if(has_none_deep(DATA[index], 
                    FUNCTION)):
                return False
        if(FUNCTION(DATA[index])):
            return False
    return True

def has_some_deep(DATA:list|dict, 
        FUNCTION)->bool:
    """
    Verifica si alguno de los elementos 
    del dato cumplen la condicion.
    """
    __valid_type(DATA)
    index = None
    for i, e in enumerate(DATA):
        # altera el index dependiendo si 
        # es un dict o list
        if(type(DATA) == dict):
            index = e
        else:
            index = i
        if(type(DATA[index]) == list 
        or type(DATA[index]) == dict):
            if(has_some_deep(DATA[index], 
                    FUNCTION)):
                return True
        if(FUNCTION(DATA[index])):
            return True
    return False