

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
    print("--> find_value_test")
    r = Btpy.key_of(
        {"a":1, "b":2, "c":3}, 1)
    print(r == "a")
    r = Btpy.key_of(
        {"a":1, "b":2, "c":3}, 2)
    print(r == "b")
    try:
        r = Btpy.key_of(
        [1, 2], 2)
    except Exception as e:
        print(True, e)
    try:
        r = Btpy.key_of(
        {"a":1, "b":2, "c":3}, 4)
    except Exception as e:
        print(True, e)

main()