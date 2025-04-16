


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
    print("--> is_error_test")
    print(Btpy.is_error_return(None) == True)
    print(Btpy.is_error_return([]) == True)
    print(Btpy.is_error_return({}) == True)
    print(Btpy.is_error_return("") == True)

main()