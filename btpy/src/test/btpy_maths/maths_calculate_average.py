

import sys
import os

# Obtiene la ruta absoluta del directorio del script actual.
directorio_actual = os.path.dirname(os.path.abspath(__file__))

# Sube dos niveles en la jerarquía de directorios.
directorio_padre = os.path.dirname(directorio_actual)
directorio_abuelo = os.path.dirname(directorio_padre)

# Añade el directorio abuelo al sys.path.
sys.path.append(directorio_abuelo)

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