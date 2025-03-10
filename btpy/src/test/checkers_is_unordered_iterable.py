

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
    r = Btpy.is_unordered_iterable({1, 2})
    print(r == True)
    r = Btpy.is_unordered_iterable(
        {"a":1, "b":2})
    print(r == True)
    r = Btpy.is_unordered_iterable((1, 2, 3))
    print(r == False)

main()