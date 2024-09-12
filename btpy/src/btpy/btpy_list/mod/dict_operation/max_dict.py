


def max_dict(dict:dict[int|float])\
    ->int|float:
    """
    Calcula el valor máximo en un 
    diccionario.
    """
    maximo = None
    for valor in dict.values():
        if((maximo is None) 
        or (valor > maximo)):
            maximo = valor
    for k in dict:
        if(dict[k] == maximo):
            return k
    return ""

