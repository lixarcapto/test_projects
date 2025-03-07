

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
    print("--> is_rgb_test")
    #
    r = Btpy.is_RGBA([255, 255, 255, 0.4])
    print(r == True)
    #
    r = Btpy.is_RGBA([255, 255, 255, 255])
    print(r == False)
    #
    r = Btpy.is_RGBA([255, 255, 255, 0])
    print(r == True)
    #
    r = Btpy.is_RGBA([255, 255, 255, 0.999])
    print(r == True)
    #
    r = Btpy.is_RGBA([255, 255, 255, 1])
    print(r == True)
    #
    r = Btpy.is_RGBA([256, 255, 255, 0.4])
    print(r == False)
    #
    r = Btpy.is_RGBA([255, 255, 255, -1])
    print(r == False)
    #
    r = Btpy.is_RGBA([255, 255, -255, 0])
    print(r == False)
    #

main()