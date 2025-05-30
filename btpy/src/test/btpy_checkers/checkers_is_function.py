


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
    r = Btpy.is_function(lambda e:e)
    print(r == True)
    def fn():
        return None
    r = Btpy.is_function(fn)
    print(r == True)
    class Test:
        def method(self):
            return None
    object_test = Test()
    r = Btpy.is_function(
        object_test.method)
    print(r == True)
    r = Btpy.is_function(4)
    print(r == False)
    r = Btpy.is_function(object_test)
    print(r == False)

main()