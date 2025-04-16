


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
    r = Btpy.center_rectangle([0, 0],
        100, 100)
    r = [50, 50] == r
    print(r == True)
    try:
        r = Btpy.center_rectangle([0, 0, 0],
        100, 100)
    except Exception as e:
        print(e)
    try:
        r = Btpy.center_rectangle([0, 0],
        "100", 100)
    except Exception as e:
        print(e)
    try:
        r = Btpy.center_rectangle([0, 0],
        100, "100")
    except Exception as e:
        print(e)
    try:
        r = Btpy.center_rectangle([0, 0],
        0, 100)
    except Exception as e:
        print(e)
    try:
        r = Btpy.center_rectangle([0, 0],
        100, 0)
    except Exception as e:
        print(e)
main()