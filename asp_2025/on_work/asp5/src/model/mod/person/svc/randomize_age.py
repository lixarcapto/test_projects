


import random

"""
    Funcion que genera un rango de edad aleatorio
    entre el rango inicial y el limite.
"""
def randomize_age(data):
    return random.randint(
        data.INITIAL_RANGE_AGE,
        data.AGE_RANGE_LIMIT
    )
