

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