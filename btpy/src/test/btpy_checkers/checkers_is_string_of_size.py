


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
    print("-- is string of 4 size")
    r = Btpy.is_string_of_size("lion", 4)
    print(r == True)
    print("-- is not string")
    r = Btpy.is_string_of_size(4, 4)
    print(r == False)
    print("-- string has not size 4")
    r = Btpy.is_string_of_size("lizard", 4)
    print(r == False)
    print("-- string is void")
    r = Btpy.is_string_of_size("", 0)
    print(r == True)

main()