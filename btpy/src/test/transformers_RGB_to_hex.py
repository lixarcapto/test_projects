

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
    r = Btpy.RGB_to_hex((0, 0, 0))
    print(r == "#000000")
    r = Btpy.RGB_to_hex((255, 255, 255))
    print(r == "#ffffff")

main()