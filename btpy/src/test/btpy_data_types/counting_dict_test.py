
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
    # count test
    counting = Btpy.CountingDict()
    counting.count("a")
    counting.count("a")
    print(counting.get()["a"] == 2)
    # count list
    counting = Btpy.CountingDict()
    counting.count_list([
        "a",
        "b",
        "c",
        "b",
        "b"
    ])
    print(counting.get()["b"] == 3)

main()