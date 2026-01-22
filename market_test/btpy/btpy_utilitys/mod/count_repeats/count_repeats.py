


def count_repeats(array:list)\
        ->dict[int]:
    """
    Función que cuenta el número 
    repeticiones de un dato en el 
    array enviado, retornando un 
    diccionario con la información 
    resultante.
    """
    dict = {}
    e_str = None
    for e in array:
        e_str = str(e)
        if(not e_str in dict):
            dict[e_str] = 1
        else:
            dict[e_str] += 1
    return dict