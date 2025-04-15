

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
    text = Btpy.TextArea(
        window, "write something")
    text.pack()
    text.set_size(10, 5)
    label = Btpy.Label(window)
    label.pack()
    btn = Btpy.Button(window, 
        "is it ready")
    btn.pack()
    def fn(e):
        txt = text.get_value()
        label.set_title(txt)
    btn.add_listener(fn)
    window.start()

main()