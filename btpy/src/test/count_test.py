

import sys
import os

# Obtiene el directorio del script actual
current_dir = os.path.dirname(os.path.abspath(__file__))
# Obtiene el directorio padre
parent_dir = os.path.dirname(current_dir)
# Agrega el directorio padre a sys.path
sys.path.append(parent_dir)

from btpy.Btpy import Btpy

def test_basic():
    # prueba si cuenta correctamente
    r = Btpy.count_true_checks(
        ["a", "b", "d", "a", "b", "a"],
        lambda e:e == "a"
    )
    print(r == 3)
    #-----------------------------------
    # prueba si cuenta correctamente
    r = Btpy.count_true_checks(
        ["a", "b", "d", "a", "b", "a"],
        lambda e:e == "a"
    )
    print(r == 3)

def negative_test():
    #------------------------------
    try:
        r = Btpy.count_true_checks(
            "[1, 2, 3, 4]",
            lambda e:e == "a"
        )
    except Exception as e:
        print(True,  e)
    #-------------------------------
    try:
        r = Btpy.count_true_checks(
            ["a", "b", "d", "a", "b", "a"],
            lambda e:e
        )
    except Exception as e:
        print(True, e)

def main():
    test_basic()
    negative_test()

main()