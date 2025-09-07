


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
    label = Btpy.ButtonIcon(
        window.widget,
        "./res/chica_pirata_1.png",
        [300, 300]
    )
    label.grid(1, 0)
    window.start()

main()