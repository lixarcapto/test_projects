

import random

"""
    Funcion que genera numeros aleatorios que no se
    encuentran en la lista enviada y en el rango
    maximo enviado, usando random libreria.
    ALG:
    * repite en un bucle el randomint funcion hasta
    obtener un numero que no este en la lista enviada.
"""
# return int
def random_int_different_from(number_list, maximum):
    random_number = 0
    while(True):
        random_number = random.randint(0, maximum)
        if(not random_number in number_list):
            return random_number
