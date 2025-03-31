

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
    window = Btpy.Window("titulo")
    window.set_is_fullscreen(True)
    box = Btpy.ButtonBoxIcon(window, 
                "frutas")
    box.create_button_dict(
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