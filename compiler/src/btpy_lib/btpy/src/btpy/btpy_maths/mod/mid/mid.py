


def mid(array:list)->float:
    """
    Función que calcula el
    promedio de los números en
    la matriz enviada.
    """
    sum_number:int = 0
    for e in array:
        sum_number += e
    return sum_number / len(array)




