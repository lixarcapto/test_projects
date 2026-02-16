

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
    # Genera un número aleatorio entre 0.0 (inclusive) y 100.0 (exclusive)
    numero_aleatorio = random.uniform(0, 100)
    # Si el número aleatorio es menor que la probabilidad deseada, retorna True
    return numero_aleatorio < porcentage

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
