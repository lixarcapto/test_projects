

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
    print("--> fit_list_test")

    r = Btpy.fit([0, 1, 2], 4)
    print(r == [0, 1, 2, None])

    r = Btpy.fit("abc", 4)
    print(r == "abc ")

    r = Btpy.fit([0, 1, 2, 4], 3)
    print(r == [0, 1, 2])

    print("")

main()