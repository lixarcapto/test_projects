


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
    switch = Btpy.SwitchIcon(
        window.widget, "pirata"
    )
    switch.set_range_size([300, 300])
    switch.set_unseleted_image_path(
        "./res/chica_normal_3.png"
    )
    switch.set_seleted_image_path(
        "./res/chica_pirata_1.png"
    )
    switch.grid(0, 0)
    window.start()

main()