
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
    print("--> max_dict_test")

    r = Btpy.max_key({"a":1, "b":2, "c":3})
    print(r == "c")

    r = Btpy.max_key({"a":5, "b":5, "c":3})
    print(r == "a")

    r = Btpy.max_key({"a":-6, "b":8, "c":5})
    print(r == "b")
    # si son float cercanos
    r = Btpy.max_key(
        {"a":1.001, "b":1.002, "c":1.003})
    print(r == "c")
    # si son todos iguales
    r = Btpy.max_key({"a":1, "b":1, "c":1})
    print(r == "a")
    # si no es dict
    try:
        r = Btpy.max_key(
            [1, 2, 3])
    except Exception as e:
        print(True, e)
    # si no el dict no es un number
    try:
        r = Btpy.max_key(
            {"a":"-6", "b":"8", "c":"5"})
    except Exception as e:
        print(True, e)
    print("")

main()