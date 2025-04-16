

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
    r = Btpy.is_point_in_rect([2, 5],
        [0, 0], 100, 100)
    print(r == True)
    r = Btpy.is_point_in_rect([0, 0],
        [0, 0], 100, 100)
    print(r == True)
    r = Btpy.is_point_in_rect([101, 101],
        [0, 0], 100, 100)
    print(r == False)
    try:
        r = Btpy.is_point_in_rect([0],
        [0, 0], 100, 100)
    except Exception as e:
        print(e)
    try:
        r = Btpy.is_point_in_rect([0, 0],
        [0], 100, 100)
    except Exception as e:
        print(e)
    try:
        r = Btpy.is_point_in_rect([0, 0],
        [0, 0], 100, "100")
    except Exception as e:
        print(e)
    try:
        r = Btpy.is_point_in_rect([0, 0],
        [0, 0], "100", 100)
    except Exception as e:
        print(e)

main()