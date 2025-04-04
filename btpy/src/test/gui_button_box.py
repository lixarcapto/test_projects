

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
    box = Btpy.ButtonBox(window, "frutas",
        ["manzana", "pera", "uvas", "mora"]
    )
    box.pack()
    def fn(key):
        print(key)
    box.add_single_listener(fn)
    box2 = Btpy.ButtonBox(window, "frutas",
        ["manzana", "pera", "uvas", "mora"]
    )
    box2.pack()
    def fn(e):
        print("el boton es pera")
    box2.add_listener_to("pera", fn)
    window.start()

main()