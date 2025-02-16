


def min_dict(dict:dict[int|float])\
    ->int|float:
    """
    Calcula la clave del valor mínimo 
    en un diccionario.
    """
    minimo = None
    clave_minima = ""
    for clave, valor in dict.items():
        if ((minimo is None) 
        or (valor < minimo)):
            minimo = valor
            clave_minima = clave
    return clave_minima