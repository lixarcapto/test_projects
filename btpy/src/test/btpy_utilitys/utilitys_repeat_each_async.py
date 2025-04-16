
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
    def fn(n):
        print("async hola")
        if(n == 5): return True
    Btpy.repeat_each_async(5, fn)
    def fn(n):
        print("sync hola")
        if(n == 5): return True
    Btpy.repeat_each(3, fn)

main()