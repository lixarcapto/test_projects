

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
    frame = Btpy.AccordionFrame(window, 
        "acordeon")
    frame.pack()
    frame.set_activated_by_mouseenter(True)
    button = Btpy.Button(
        frame, "click")
    button.pack()
    def fn(e):
        print("funciona")
    button.add_listener(fn)
    window.start()

main()