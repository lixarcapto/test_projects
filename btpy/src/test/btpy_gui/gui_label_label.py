

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
    label_list = []
    label = None
    for i in range(6):
        label = Btpy.LabelLabel(window, 
        "nombre")
        label.set_font_size(16)
        label.set_content("Juan")
        label.set_content_foreground_color("white")
        label.set_content_background_color("blue")
        label.draw_in_direction()
        label_list.append(label)
    window.start()

main()