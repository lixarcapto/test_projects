

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
    selector_box = Btpy.SelectorBox(
        window, 
            "animal favorito", [
                "gato",
                "tortuga",
                "perro",
                "oso",
                "lagartija"
            ]
    )
    selector_box.pack()
    label = Btpy.Label(window, "")
    label.pack()
    button = Btpy.Button(window, 
                         "get data")
    button.pack()
    def fn():
        k_list = selector_box.get_value()
        label.set_title(k_list)
    button.add_listener(fn)
    window.start()

main()