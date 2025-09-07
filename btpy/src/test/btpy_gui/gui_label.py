

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
    label = Btpy.Label(window, "texto")
    label.draw_in_direction()
    label.set_font_size(17)
    label.set_is_bold(True)
    label.set_font_family("Verdana")
    label.add_mouse_leave_listener(
        lambda e:print("leave")
    )
    window.start()

main()