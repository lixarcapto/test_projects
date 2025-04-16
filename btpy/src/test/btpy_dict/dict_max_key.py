
import sys
import os

# Obtiene la ruta absoluta del directorio del script actual.
directorio_actual = os.path.dirname(os.path.abspath(__file__))
# Sube dos niveles en la jerarquía de directorios.
directorio_padre = os.path.dirname(directorio_actual)
directorio_abuelo = os.path.dirname(directorio_padre)
# Añade el directorio abuelo al sys.path.
sys.path.append(directorio_abuelo)

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