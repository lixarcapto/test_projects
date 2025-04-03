

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
    button = Btpy.BinaryButtonDouble(
        window, "opciones", 
        ["si", "no"]
    )
    button.pack()
    def fn(e):
        print(button.get_value())
    button.add_listener(fn)
    window.start()

main()