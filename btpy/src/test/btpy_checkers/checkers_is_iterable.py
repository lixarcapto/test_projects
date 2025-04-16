

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
    r = Btpy.is_iterable("abcd")
    print(r == True)
    r = Btpy.is_iterable([0,1,0,1])
    print(r == True)
    r = Btpy.is_iterable({"a":0, "b":1})
    print(r == True)
    r = Btpy.is_iterable({1, 2, 3, 4})
    print(r == True)
    r = Btpy.is_iterable((1, 2, 3, 4))
    print(r == True)
    r = Btpy.is_iterable(1)
    print(r == False)
    r = Btpy.is_iterable(1.5)
    print(r == False)
    class Test:
        def __init__(self):
            pass
    r = Btpy.is_iterable(Test)
    print(r == False)
    r = Btpy.is_iterable(Test())
    print(r == False)

main()