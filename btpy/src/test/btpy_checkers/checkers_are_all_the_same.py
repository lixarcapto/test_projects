


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
    r = Btpy.are_all_the_same([0, 1, 0])
    print(r == False)
    r = Btpy.are_all_the_same([0, 0, 0])
    print(r == True)
    r = Btpy.are_all_the_same([0])
    print(r == True)

main()
