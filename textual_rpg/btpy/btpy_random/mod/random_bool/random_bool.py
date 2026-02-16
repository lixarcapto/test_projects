

import random


def random_bool() -> bool:
    """
    Función que genera un dato boolean 
    aleatorio
    """
    if(random.randint(0, 1) == 0):
        return False
    return True
