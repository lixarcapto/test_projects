


def clean_voids(ARRAY : list)->list:
    """
    TESTED
    Función que crea un nuevo array
    eliminando todos los valores de tipo
    None y void como void string "",
    void array [], y void dict {}
    """
    new_array:list = []
    for i in range(len(ARRAY)):
        if(ARRAY[i] == None): continue
        if(ARRAY[i] == ""): continue
        if(ARRAY[i] == []): continue
        if(ARRAY[i] == {}): continue
        new_array.append(ARRAY[i])
    return new_array