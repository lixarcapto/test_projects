

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
    #"es un rango entero"
    r = Btpy.is_range([0, 1])
    #"es un rango float"
    r = Btpy.is_range([0.1, 1.2])
    print(r == True)
    #"no existe rango"
    r = Btpy.is_range([1, 1])
    print(r == False)
    #"si el rango esta invertido"
    r = Btpy.is_range([5, 1])
    print(r == False)
    #"no es array"
    r = Btpy.is_range(2)
    print(r == False)
    #"es texto"
    r = Btpy.is_range("[0, 1]")
    print(r == False)

main()