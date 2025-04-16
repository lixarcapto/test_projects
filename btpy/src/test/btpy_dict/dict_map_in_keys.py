


import sys
import os

# Obtiene la ruta absoluta del directorio del script actual.
directorio_actual = os.path.dirname(os.path.abspath(__file__))
# Sube dos niveles en la jerarquía de directorios.
directorio_padre = os.path.dirname(directorio_actual)
directorio_abuelo = os.path.dirname(directorio_padre)
# Añade el directorio abuelo al sys.path.
sys.path.append(directorio_abuelo)

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