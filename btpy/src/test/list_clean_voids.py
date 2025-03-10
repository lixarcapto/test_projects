

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
    print("--> clean_voids_test")
    #
    r = Btpy.clean_voids(["a", "b", ""])
    print(r == ["a", "b"])
    #
    r = Btpy.clean_voids([0, 1, None, 2])
    print(r == [0, 1, 2])
    #
    r = Btpy.clean_voids([[0], [1], [], [2]])
    print(r == [[0], [1], [2]])
    #

main()