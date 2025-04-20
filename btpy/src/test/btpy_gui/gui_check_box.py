

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
    checkbox = Btpy.CheckBox(window,
        True, 
        "elige")
    checkbox.set_content(text_list)
    checkbox.pack()
    button = Btpy.Button(window, "send")
    button.pack()
    def fn(e):
        i_list = checkbox.get_value()
        for i in i_list:
            print(text_list[i])
    button.add_listener(fn)
    window.start()

main()