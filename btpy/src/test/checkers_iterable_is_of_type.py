

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
    # si es array int
    r = Btpy.iterable_is_of_type(
        [1, 2, 3, 4],
        int)
    print(r == True)
    # si es array float
    r = Btpy.iterable_is_of_type(
        [1.1, 2.1, 3.1],
        float)
    print(r == True)
    # si es array string
    r = Btpy.iterable_is_of_type(
        ["1.1", "2.1", "3.1"],
        str)
    print(r == True)
    # si es array list
    r = Btpy.iterable_is_of_type(
        [[1], [1], [1]],
        list)
    # si es array dict
    r = Btpy.iterable_is_of_type(
        [{}, {}, {}],
        set)
    # si es array float
    r = Btpy.iterable_is_of_type(
        [{"a":1}, {"a":1}, {"a":1}],
        dict)
    # si es array dict
    r = Btpy.iterable_is_of_type(
        [(), (), ()],
        tuple)
    print(r == True)
    # si no es iterable
    r = Btpy.iterable_is_of_type(
        5,
        int)
    print(r == False)
    # si no es int
    r = Btpy.iterable_is_of_type(
        ["a", "b", "c"],
        int)
    print(r == False)
    # si es mixto de string int
    r = Btpy.iterable_is_of_type(
        ["a", "b", 1, 3],
        int)
    print(r == False)

main()