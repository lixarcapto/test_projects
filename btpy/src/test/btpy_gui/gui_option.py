

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
    label = Btpy.Label(window, "")
    label.pack()
    option = Btpy.Option(window, "option")
    option.set_content(
        "Te gusta esta aplicacion?",
        "si",
        "no"
    )
    def fn(answer):
        if(answer):
            label.set_title("te gusta :)")
        else:
            label.set_title("no te gusta :q")
    option.add_listener(fn)
    option.pack()
    window.start()

main()