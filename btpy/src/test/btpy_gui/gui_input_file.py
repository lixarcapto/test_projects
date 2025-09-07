

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
    file = Btpy.InputFile(window,
            "image", 
            "busca image")
    file.draw_in_direction(False, "top")
    def fn(e):
        print("postselection event")
    file.add_listener_onchange(fn)
    file2 = Btpy.InputFile(window,
            "folder", 
            "busca folder")
    file2.draw_in_direction(False, "top")
    file3 = Btpy.InputFile(window,
            "text", 
            "busca text")
    file3.draw_in_direction(False, "top")
    file4 = Btpy.InputFile(window,
            "any_file", 
            "busca any file")
    file4.draw_in_direction(False, "top")
    window.start()

main()