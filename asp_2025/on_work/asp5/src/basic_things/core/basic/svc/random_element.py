

from ..dependences import random

"""
    Funcion que elige un elemento aleatorio de un array
    y lo retorna.
"""
# return tipo del array
def random_element(array):
    if(not len(array) > 0):
        print("=>Error: void array from LogicFacade.random_element_from_array")
        return None
    # Obtener un índice aleatorio dentro del rango del array
    indice_aleatorio = random.randint(0, len(array) - 1)
    # Devolver el elemento del array en el índice aleatorio
    return array[indice_aleatorio]
