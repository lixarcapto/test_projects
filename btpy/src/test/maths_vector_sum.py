


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
    r = Btpy.vector_sum(
        [1, 2, 1], [1, 2, 1])
    print(r == [2, 4, 2])
    # si array1 no es array
    try:
        r = Btpy.vector_sum(
        5, [1, 2, 1])
    except Exception as e:
        print(True)
        print(e)
    # si array2 no es array
    try:
        r = Btpy.vector_sum(
        [1, 2, 1], 5)
    except Exception as e:
        print(True)
        print(e)
    # si array1 no es iterable numerico
    try:
        r = Btpy.vector_sum(
        [1, 2, 1], ["1", "2", "1"])
    except Exception as e:
        print(True)
        print(e)
    # si array2 no es iterable numerico
    try:
        r = Btpy.vector_sum(
        ["1", "2", "1"], [1, 2, 1])
    except Exception as e:
        print(True)
        print(e)
    # si el array1 y el array2 no son 
    # del mismo tamaño.
    try:
        r = Btpy.vector_sum(
        [1, 2, 1], [1, 2, 1, 2])
    except Exception as e:
        print(True)
        print(e)
    

main()