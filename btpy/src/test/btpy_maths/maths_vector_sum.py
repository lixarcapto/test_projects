


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
    r = Btpy.vector_sum(
        [1, 2, 1], [1, 2, 1])
    print(r == [2, 4, 2])
    # si array1 no es array
    try:
        r = Btpy.vector_sum(
        5, [1, 2, 1])
    except Exception as e:
        print(True)
        print(e)
    # si array2 no es array
    try:
        r = Btpy.vector_sum(
        [1, 2, 1], 5)
    except Exception as e:
        print(True)
        print(e)
    # si array1 no es iterable numerico
    try:
        r = Btpy.vector_sum(
        [1, 2, 1], ["1", "2", "1"])
    except Exception as e:
        print(True)
        print(e)
    # si array2 no es iterable numerico
    try:
        r = Btpy.vector_sum(
        ["1", "2", "1"], [1, 2, 1])
    except Exception as e:
        print(True)
        print(e)
    # si el array1 y el array2 no son 
    # del mismo tamaño.
    try:
        r = Btpy.vector_sum(
        [1, 2, 1], [1, 2, 1, 2])
    except Exception as e:
        print(True)
        print(e)
    

main()