


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
    window.set_size(1000, 700)
    window.set_path_image(
        "./res/chica_pirata_1.png"
    )
    label = Btpy.Label(window.widget,
        "Chica Pirata")
    label.place(100, 100)
    window.start()

main()