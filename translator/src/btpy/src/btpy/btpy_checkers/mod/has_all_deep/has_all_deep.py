
def has_all_deep(DATA, FUNCTION)->bool:
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

def has_none_deep(DATA, FUNCTION)->bool:
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

def has_some_deep(DATA, FUNCTION)->bool:
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