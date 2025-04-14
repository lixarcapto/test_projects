

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
    label = Btpy.Label(window, "")
    label.pack()
    option = Btpy.Option(window, "option")
    option.set_content(
        "Te gusta esta aplicacion?",
        "si",
        "no"
    )
    def fn(answer):
        if(answer):
            label.set_title("te gusta :)")
        else:
            label.set_title("no te gusta :q")
    option.add_listener(fn)
    option.pack()
    window.start()

main()