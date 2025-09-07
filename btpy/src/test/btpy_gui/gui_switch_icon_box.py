

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
    box = Btpy.SwitchIconBox(window,
                False, 
                "Switch icon box")
    box.set_components(4, 1)
    box.set_path_list_false([
            "./res/cell.png",
            "./res/cell.png",
            "./res/cell.png",
            "./res/cell.png"
        ]
        
    )
    box.set_path_list_true([
            "./res/feto_100x100.png",
            "./res/feto_100x100.png",
            "./res/feto_100x100.png",
            "./res/feto_100x100.png"
        ]
        
    )
    box.draw_in_direction()
    print("box iniciado")
    def fn(key):
        print(key)
    box.add_single_listener(fn)
    window.start()

main()