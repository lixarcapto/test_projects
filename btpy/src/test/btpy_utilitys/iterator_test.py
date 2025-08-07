

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

def test_get_size():
    it = Btpy.Iterator(
        [1, 2, 3, 4, 5, 6]
    )
    print("test_get_size",
        it.get_size() == 6)

def test_next():
    it = Btpy.Iterator(
        [1, 2, 3, 4, 5, 6]
    )
    while(it.has_next()):
        it.next()
    print("test_next",
        6 == it.get())
    
def test_next_reverse():
    it = Btpy.Iterator(
        [1, 2, 3, 4, 5, 6]
    )
    it.set_is_reverse(True)
    it.reset()
    while(it.has_next()):
        print(it.get())
        it.next()
    print("test_next_reverse",
        1 == it.get())
    
def test_next_cicle():
    it = Btpy.Iterator(
        [1, 2, 3, 4, 5, 6]
    )
    it.set_is_cycle(True)
    for i in range(12):
        it.next()
    print("test_next_cicle",
        1 == it.get())

def main():
    test_get_size()
    test_next()
    test_next_reverse()
    test_next_cicle()

main()