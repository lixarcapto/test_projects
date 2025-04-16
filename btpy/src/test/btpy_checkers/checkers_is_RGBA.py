

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
    print("--> is_rgb_test")
    #
    r = Btpy.is_RGBA([255, 255, 255, 0.4])
    print(r == True)
    #
    r = Btpy.is_RGBA([255, 255, 255, 255])
    print(r == False)
    #
    r = Btpy.is_RGBA([255, 255, 255, 0])
    print(r == True)
    #
    r = Btpy.is_RGBA([255, 255, 255, 0.999])
    print(r == True)
    #
    r = Btpy.is_RGBA([255, 255, 255, 1])
    print(r == True)
    #
    r = Btpy.is_RGBA([256, 255, 255, 0.4])
    print(r == False)
    #
    r = Btpy.is_RGBA([255, 255, 255, -1])
    print(r == False)
    #
    r = Btpy.is_RGBA([255, 255, -255, 0])
    print(r == False)
    #

main()