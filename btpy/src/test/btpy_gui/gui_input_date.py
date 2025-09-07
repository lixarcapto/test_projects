

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
    date = Btpy.InputDate(window, "date")
    date.set_recomended_years([
        "2000",
        "2001"
    ])
    date.draw_in_direction()
    btn = Btpy.Button(window, "get date")
    btn.draw_in_direction()
    label = Btpy.Label(window, "")
    label.draw_in_direction()
    def fn(e):
        label.set_title(date.get_value())
        print("button event")
    btn.add_listener(fn)
    window.start()

main()