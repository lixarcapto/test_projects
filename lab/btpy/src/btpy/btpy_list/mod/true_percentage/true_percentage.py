


def true_percentage(array:list[bool])\
        ->float:
    """
    Función que calcula el 
    porcentaje de datos verdaderos 
    de una lista booleana
    """ 
    true_number = 0
    for e in array:
        if(e): true_number += 1
    percent = true_number * \
        (100 / len(array))
    percent = float(percent)
    return percent