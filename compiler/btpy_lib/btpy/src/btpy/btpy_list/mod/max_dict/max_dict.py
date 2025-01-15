


def max_dict(dict:dict[int|float])\
    ->str:
    """
    Calcula el valor máximo en un 
    diccionario y retorna la clave de ese
    valor. Si hay dos valores iguales
    usa el que esta primero en el orden
    del diccionario.
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

