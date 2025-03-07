


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
    print("--> is_point_test")
    test_is_point()
    test_is_not_point()
    
    
def test_is_not_point():
    print("--if is array x1")
    r = Btpy.is_point_2D([0])
    print(r == False)
    print("--if is array x3")
    r = Btpy.is_point_2D([0, 0, 0])
    print(r == False)
    print("--if is string")
    r = Btpy.is_point_2D("[0, 0]")
    print(r == False)

def test_is_point():
    print("--if is point 2D")
    r = Btpy.is_point_2D([0, 0])
    print(r == True)
    print("--if is point 2D negative")
    r = Btpy.is_point_2D([-5, -7])
    print(r == True)
    print("--if is point 2D float")
    r = Btpy.is_point_2D([0.4, 2.6])
    print(r == True)

main()
