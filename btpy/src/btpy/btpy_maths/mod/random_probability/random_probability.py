

import random


def random_probability(porcentage: int)\
    -> bool:
    """
    Funcion que genera un boolean 
    aleatorio basado en el porcentaje 
    enviado.
    """
    valid_porcentage(porcentage)
    if porcentage == 100: return True
    if porcentage == 0: return False
    numero = random.randint(0, 
        100 - porcentage)
    result = False
    if numero == 1: result = True
    return result

def valid_porcentage(porcentage):
    if(not type(porcentage) == type(0)):
        raise Exception(
            "porcentage is not integer"
          )
    if(porcentage > 100):
        raise Exception(
            "porcentage greater than 100%"
        )
    if(porcentage < 0):
        raise Exception(
            "porcentage less than 0%"
        )
