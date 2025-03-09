

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
    r = Btpy.calculate_average(
        [1, 2, 3, 2, 2, 1, 2, 3]
    )
    print(r)
    r = Btpy.calculate_average(
        (1, 2, 3, 2, 2, 1, 2, 3)
    )
    print(r)
    r = Btpy.calculate_average(
        {1, 2, 3, 4, 5}
    )
    print(r)
    r = Btpy.calculate_average(
        {"a":2, "b":3, "c":3, "d":2, "f":3}
    )
    print(r)
    # si no es iterable
    try:
        r = Btpy.calculate_average(
            5
        )
    except Exception as e:
        print(True)
        print(e)
    # si el iterable no es numerico
    try:
        r = Btpy.calculate_average(
            ["a", "b", "c"]
        )
    except Exception as e:
        print(True)
        print(e)

main()