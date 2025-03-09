

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
    r = Btpy.is_iterable("abcd")
    print(r == True)
    r = Btpy.is_iterable([0,1,0,1])
    print(r == True)
    r = Btpy.is_iterable({"a":0, "b":1})
    print(r == True)
    r = Btpy.is_iterable({1, 2, 3, 4})
    print(r == True)
    r = Btpy.is_iterable((1, 2, 3, 4))
    print(r == True)
    r = Btpy.is_iterable(1)
    print(r == False)
    r = Btpy.is_iterable(1.5)
    print(r == False)
    class Test:
        def __init__(self):
            pass
    r = Btpy.is_iterable(Test)
    print(r == False)
    r = Btpy.is_iterable(Test())
    print(r == False)

main()