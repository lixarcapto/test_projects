

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
    rect_1 = {
        "x": 0,
        "y": 0,
        "width": 100,
        "height": 100
    }
    rect_2 = {
        "x": 50,
        "y": 50,
        "width": 100,
        "height": 100
    }
    r = Btpy.is_colliding_rect(
        rect_1, rect_2
    )
    print(r == True)
    rect_1 = {
        "x": 0,
        "y": 0,
        "width": 100,
        "height": 100
    }
    rect_2 = {
        "x": 101,
        "y": 101,
        "width": 100,
        "height": 100
    }
    r = Btpy.is_colliding_rect(
        rect_1, rect_2
    )
    print(r == False)
    try:
        r = Btpy.is_colliding_rect(
            {}, rect_2
        )
    except Exception as e:
        print(e)
    try:
        r = Btpy.is_colliding_rect(
            rect_1, {}
        )
    except Exception as e:
        print(e)

main()
