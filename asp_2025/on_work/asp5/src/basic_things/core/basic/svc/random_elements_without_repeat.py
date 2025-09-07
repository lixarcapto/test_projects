

from ..dependences import random

"""
    Funcion que randomiza elementos de un array
    sin repetirlos en la cantidad indicada.
"""
# return array
def random_elements_without_repeat(\
    array, quantity):
    # Validar la cantidad
    if quantity > len(array):
        print("=>Error cantidad mayor que el array: \
        in basic_things.randomize_elements_of_an_array_without_repeating")
        raise ValueError(\
            "La cantidad solicitada supera la longitud del array")
    # Copiar el array original para no modificarlo
    array_copia = array.copy()
    # Mezclar el array aleatoriamente
    random.shuffle(array_copia)
    # Devolver los primeros `cantidad` elementos del array mezclado
    return array_copia[:cantidad]
