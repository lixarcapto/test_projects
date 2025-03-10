


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
    r = Btpy.filter([1, 2, 1, 0, 1],
        lambda e: e==1)
    print(r == [1, 1, 1])
    r = Btpy.filter([1, 2, 1, 0, 1],
        lambda e: e==2)
    print(r == [2])
    r = Btpy.filter([1, 2, 1, 0, 1],
        lambda e: e==3)
    print(r == [])
    # si ITERABLE no es un iterable
    try:
        r = Btpy.filter(2,
            lambda e: e==1)
    except Exception as e:
        print(True, e)
    # si FUNCTION no es una funcion
    try:
        r = Btpy.filter([1, 2, 1, 0, 1],
            2)
    except Exception as e:
        print(True, e)

main()