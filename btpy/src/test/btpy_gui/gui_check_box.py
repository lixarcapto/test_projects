

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
    text_list = [
            "axxx", "bxxx", "cxxx", "dxxx"
        ]
    key_list = [
            "a", "b", "c", "d"
        ]
    checkbox = Btpy.CheckBox(window,
        True, 
        "elige")
    checkbox.set_components(key_list)
    checkbox.set_content(text_list)
    checkbox.draw_in_direction()
    button = Btpy.Button(window, "send")
    button.draw_in_direction()
    def fn(e):
        print(checkbox.get_value())
        checkbox.set_columns(1)
    button.add_listener(fn)
    window.start()

main()