


import sys
import os

# Obtiene el directorio del script actual
current_dir = os.path.dirname(os.path.abspath(__file__))
# Obtiene el directorio padre
parent_dir = os.path.dirname(current_dir)
# Agrega el directorio padre a sys.path
sys.path.append(parent_dir)

from btpy.Btpy import Btpy

def main():
    print("--> map_in_keys_test")

    r = Btpy.map_in_keys({"a":0, "b":0},
        lambda e:e + ".")
    
    print(r == {"a.":0, "b.":0})

    # si no es un diccionario
    try:
        r = Btpy.map_in_keys([1, 2, 3],
        lambda e:e)
    except Exception as e:
        print(True, e)

    # si no es una funcion
    try:
        r = Btpy.map_in_keys(
            {"a":0, "b":0},
            2
        )
    except Exception as e:
        print(True, e)

    print("")

main()