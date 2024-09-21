


def fit_list(LIST, SIZE, 
        FILL_TYPE = None)->list:
    """
    Funcion que ajusta la lista enviada 
    al tamaño indicado.
    """
    new_list = []
    for i in range(SIZE):
        if(i >= len(LIST)):
            new_list.append(FILL_TYPE)
        else:
            new_list.append(LIST[i])
    return new_list