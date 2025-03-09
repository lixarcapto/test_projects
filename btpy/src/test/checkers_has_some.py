

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
    print("--> has_some_test")
    # prueba si funciona
    r = Btpy.has_some([1, 2, 1], 
                     lambda e:e == 2)
    print(r == True)
    r = Btpy.has_some([1, 1, 1], 
                     lambda e:e == 2)
    print(r == False)
    # si ITERABLE no es un iterable
    try:
        r = Btpy.has_some(5, 
                     lambda e:e == 1)
    except Exception as e:
        print(True)
        print(e)
    # si FUNCTION no es una funcion
    try:
        r = Btpy.has_some("abcd", 
                     5)
    except Exception as e:
        print(True)
        print(e)
    # si ITERABLE es void
    try:
        r = Btpy.has_some("", 
                     lambda e:e == 1)
    except Exception as e:
        print(True)
        print(e)

main()