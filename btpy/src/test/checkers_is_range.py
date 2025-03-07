

import sys
import os

# Obtiene el directorio del script actual
current_dir = os.path.dirname(os.path.abspath(__file__))
# Obtiene el directorio padre
parent_dir = os.path.dirname(current_dir)
# Agrega el directorio padre a sys.path
sys.path.append(parent_dir)

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