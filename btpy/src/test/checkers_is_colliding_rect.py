

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
