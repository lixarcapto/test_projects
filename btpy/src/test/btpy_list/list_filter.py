


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
    r = Btpy.filter([1, 2, 1, 0, 1],
        lambda e: e==1)
    print(r == [1, 1, 1])
    r = Btpy.filter([1, 2, 1, 0, 1],
        lambda e: e==2)
    print(r == [2])
    r = Btpy.filter([1, 2, 1, 0, 1],
        lambda e: e==3)
    print(r == [])
    # si ITERABLE no es un iterable
    try:
        r = Btpy.filter(2,
            lambda e: e==1)
    except Exception as e:
        print(True, e)
    # si FUNCTION no es una funcion
    try:
        r = Btpy.filter([1, 2, 1, 0, 1],
            2)
    except Exception as e:
        print(True, e)

main()