

"""
Función que calcula el
promedio de los números en
la matriz enviada.
"""
def calculate_mid(array:list)->float:
    sum_number:int = 0
    for e in array:
        sum_number += e
    return sum_number / len(array)




