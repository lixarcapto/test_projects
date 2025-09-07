


def true_percentage(ARRAY:list[bool])\
        ->float:
    """
    Función que calcula el 
    porcentaje de datos verdaderos 
    de una lista booleana
    """ 
    true_number = 0
    for e in ARRAY:
        if(e): true_number += 1
    percent = true_number * \
        (100 / len(ARRAY))
    percent = float(percent)
    return percent