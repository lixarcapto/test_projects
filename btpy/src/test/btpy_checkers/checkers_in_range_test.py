

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
    #
    print("esta en rango")
    r = Btpy.in_range(3, [0, 5])
    print(r == True)
    #
    print("esta en rango limite min")
    r = Btpy.in_range(0, [0, 5])
    print(r == True)
    #
    print("esta en rango limite max")
    r = Btpy.in_range(5, [0, 5])
    print(r == True)
    #
    test_is_a_range_of_1()
    #
    test_is_not_array()
    #
    test_array_is_big()
    #
    test_array_is_little()
    #
    test_array_is_not_string()

def test_is_a_range_of_1():
    r = Btpy.in_range(0, [0, 1])
    print(r == True)

def test_is_not_array():
    try:
        r = Btpy.in_range(5, 5)
    except Exception as e:
        print(True)

def test_array_is_big():
    try:
        r = Btpy.in_range(3, [0, 5, 5])
    except Exception as e:
        print(True)

def test_array_is_little():
    try:
        r = Btpy.in_range(0, [0])
    except Exception as e:
        print(True)

def test_array_is_not_string():
    try:
        r = Btpy.in_range("3", [0, 5])
    except Exception as e:
        print(True)

main()