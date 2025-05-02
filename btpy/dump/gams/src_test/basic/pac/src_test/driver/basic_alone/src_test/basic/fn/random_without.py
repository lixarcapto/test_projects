

import random

"""
    Funcion que genera un numero aleatorio 
    en el rango sin repetir los numeros 
    enviados en la lista indicando si es 
    exclusivo o no.
"""
def random_without(range: int, 
        repeated_int_ar: list,
        is_exclusive:bool = False
        ) -> int:
    result = 0
    limit = 10000
    n = 0
    if is_exclusive:
        range[0] += 1
        range[1] -= 1
    while(True):
        result = random.randint(range[0], 
                                range[1])
        if(not result in repeated_int_ar):
            return result
        if n == limit:
            raise Exception("out of limit iterations")
        n += 1
    raise Exception("random int doesnt exist")
