

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
    # si es array int
    r = Btpy.instanceof_iterable(
        [1, 2, 3, 4],
        int)
    print(r == True)
    # si es array float
    r = Btpy.instanceof_iterable(
        [1.1, 2.1, 3.1],
        float)
    print(r == True)
    # si es array string
    r = Btpy.instanceof_iterable(
        ["1.1", "2.1", "3.1"],
        str)
    print(r == True)
    # si es array list
    r = Btpy.instanceof_iterable(
        [[1], [1], [1]],
        list)
    # si es array dict
    r = Btpy.instanceof_iterable(
        [{}, {}, {}],
        set)
    # si es array float
    r = Btpy.instanceof_iterable(
        [{"a":1}, {"a":1}, {"a":1}],
        dict)
    # si es array dict
    r = Btpy.instanceof_iterable(
        [(), (), ()],
        tuple)
    print(r == True)
    # si no es iterable
    r = Btpy.instanceof_iterable(
        5,
        int)
    print(r == False)
    # si no es int
    r = Btpy.instanceof_iterable(
        ["a", "b", "c"],
        int)
    print(r == False)
    # si es mixto de string int
    r = Btpy.instanceof_iterable(
        ["a", "b", 1, 3],
        int)
    print(r == False)

main()