

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
    print("--> count_test")

    r = Btpy.count_true_checks([0, 1, 1, 1], lambda e:e==1)
    print(r == 3)

    r = Btpy.count_true_checks([0, 3, 4, 3], lambda e:e!=3)
    print(r == 2)

    r = Btpy.count_true_checks([1], lambda e:e==1)
    print(r == 1)
    # si ITERABLE no es iterable
    try:
        r = Btpy.count_true_checks(
            1, 
            lambda e:e==1
        )
    except Exception as e:
        print(True, e)
    # si CHECKER_FUNCTION no es funcion
    try:
        r = Btpy.count_true_checks(
            [1], 
            1
        )
    except Exception as e:
        print(True, e)

    print("")

main()

