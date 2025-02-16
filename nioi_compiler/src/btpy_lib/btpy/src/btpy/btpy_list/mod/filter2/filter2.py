


def filter2(ARRAY:list, FUNCTION, 
        QUANTITY:int = -1)->list:
    """
    función que busca  los 
    elementos por la condición enviada 
    en la lista.
    """
    new_array:list = []
    for i in range(len(ARRAY)):
        if(FUNCTION(ARRAY[i])):
            new_array.append(ARRAY[i])
        if(i == QUANTITY): break
    return new_array