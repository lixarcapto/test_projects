

import random

"""
Función que genera un dato boolean 
aleatorio
"""
def random_bool() -> bool:
    if(random.randint(0, 1) == 0):
        return False
    return True
