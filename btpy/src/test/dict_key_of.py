

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
    print("--> find_value_test")
    r = Btpy.key_of(
        {"a":1, "b":2, "c":3}, 1)
    print(r == "a")
    r = Btpy.key_of(
        {"a":1, "b":2, "c":3}, 2)
    print(r == "b")
    try:
        r = Btpy.key_of(
        [1, 2], 2)
    except Exception as e:
        print(True, e)
    try:
        r = Btpy.key_of(
        {"a":1, "b":2, "c":3}, 4)
    except Exception as e:
        print(True, e)

main()