


import random

"""
    Funcion wrapper para mejorar choice de random
    library añadiendo la posibilidad de randomizar
    elementos de diccionarios.
"""
# return element
def random_choice(array: list):
    if(type(array) == type([])
    or type(array) == type("")):
        return random.choice(array)
    elif(type(array) == type({})):
        key_arr = []
        for k in array:
            key_arr.append(k)
        key = random.choice(key_arr)
        return array[key]
    else:
        raise Exception("unsupported type " \
        + f"{type(array)}")
