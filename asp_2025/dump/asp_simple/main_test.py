

from btpy.src.btpy.Btpy import Btpy

# para basic things
def find_value(DICT, DATA)->str:
    """
    Busca la clave del valor enviado
    en el diccionario.
    """
    for k in DICT:
        if(DATA == DICT[k]):
            return k
    return ""

# para basic things
def find_closest_lower(DICT, NUMBER):
    """
    funcion que identifique en un 
    diccionario de numeros que numero 
    es el mas cercano inferior al numero 
    enviado retornando su clave.
    """
    values_arr = sorted(DICT.values())
    former_number:int|float = 0
    for value in values_arr:
        if(value > NUMBER):
            break
        former_number = value
    key = find_value(DICT, former_number)
    return DICT[key]

import sys

def main_test():
    None

main_test()