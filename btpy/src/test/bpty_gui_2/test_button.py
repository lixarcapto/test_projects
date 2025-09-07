


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
    btn = Btpy.Button(
        window.widget, "click")
    btn.set_font_size(15)
    btn.grid(0, 0, "")
    label = Btpy.Label(window.widget, 
            "text")
    label.grid(0, 1)
    label.set_font_size(15)
    def fn(e):
        v = label.get_title()
        v += "a"
        label.set_title(v)
    btn.add_listener(fn)
    window.start()

main()