

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
    window = Btpy.Window("titulo")
    window.set_is_fullscreen(True)
    box = Btpy.ButtonBoxIcon(window, 
                "frutas")
    box.set_content(
        ["manzana", "pera", "uvas", "mora"],
        [
            "../btpy/res/image/cell.png",
            "../btpy/res/image/cell.png",
            "../btpy/res/image/cell.png",
            "../btpy/res/image/cell.png"
        ]
        
    )
    box.pack()
    def fn(key):
        print(key)
    box.add_single_listener(fn)
    window.start()

main()