


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
    r = Btpy.center_square([0, 0],
        100, 100)
    r = [50, 50] == r
    print(r == True)
    try:
        r = Btpy.center_square([0, 0, 0],
        100, 100)
    except Exception as e:
        print(e)
    try:
        r = Btpy.center_square([0, 0],
        "100", 100)
    except Exception as e:
        print(e)
    try:
        r = Btpy.center_square([0, 0],
        100, "100")
    except Exception as e:
        print(e)
    try:
        r = Btpy.center_square([0, 0],
        0, 100)
    except Exception as e:
        print(e)
    try:
        r = Btpy.center_square([0, 0],
        100, 0)
    except Exception as e:
        print(e)
main()