

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
    r = Btpy.is_hex_color("#2596be")
    print(r == True)
    #
    r = Btpy.is_hex_color("#873e23")
    print(r == True)
    #
    r = Btpy.is_hex_color("#993300")
    print(r == True)
    #
    r = Btpy.is_hex_color("")
    print(r == False)
    #
    r = Btpy.is_hex_color("993300")
    print(r == False)
    #

main()