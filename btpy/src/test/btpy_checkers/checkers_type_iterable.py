

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
    # prueba con listas ---------------
    r = Btpy.type_iterable([1, 2, 3, 4])
    print(r == int)
    r = Btpy.type_iterable([[], [], []])
    print(r == list)
    r = Btpy.type_iterable([{1}, {2}])
    print(r == set)
    r = Btpy.type_iterable([1.0, 1.2])
    print(r == float)
    r = Btpy.type_iterable(
        [{"a":1}, {"a":2}])
    print(r == dict)
    r = Btpy.type_iterable(["1", "2", "3"])
    print(r == str)
    # --------------------------------
    # pruebas con cualquiera ---------------
    r = Btpy.type_iterable("abc")
    print(r == str)
    r = Btpy.type_iterable({1, 2, 3})
    print(r == int)
    r = Btpy.type_iterable({"a":1, "b":2})
    print(r == int)
    r = Btpy.type_iterable((1, 2))
    print(r == int)
    r = Btpy.type_iterable(("a", "b"))
    print(r == str)
    # --------------------------------
    # pruebas negativas ---------------
    # prueba si no es iterable
    try:
        r = Btpy.type_iterable(4)
    except Exception as e:
        print(True, e)
    # prueba si ITERABLE es zero
    try:
        r = Btpy.type_iterable([])
    except Exception as e:
        print(True, e)
    # prueba si es un iterable multitipo
    try:
        r = Btpy.type_iterable(("a", 1))
    except Exception as e:
        print(True, e)
    # ----------------------------------

main()