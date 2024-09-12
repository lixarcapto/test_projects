


def clean_voids(ARRAY)->list:
    """
     Función que crea un nuevo 
     eliminando todos los valores 
     None y void
    """
    new_array = []
    for i in range(len(ARRAY)):
        if(ARRAY[i] == None): continue
        if(ARRAY[i] == ""): continue
        if(ARRAY[i] == []): continue
        if(ARRAY[i] == {}): continue
        new_array.append(ARRAY[i])
    return new_array