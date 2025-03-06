


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
    r = Btpy.is_function(lambda e:e)
    print(r == True)
    def fn():
        return None
    r = Btpy.is_function(fn)
    print(r == True)
    class Test:
        def method(self):
            return None
    object_test = Test()
    r = Btpy.is_function(
        object_test.method)
    print(r == True)
    r = Btpy.is_function(4)
    print(r == False)
    r = Btpy.is_function(object_test)
    print(r == False)

main()