

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
    button = Btpy.ButtonIconText(window, 
        "click aqui")
    button.paint_image("./res/cell.png")
    button.pack()
    button.set_text_position("LEFT")
    button2 = Btpy.ButtonIconText(window, 
        "click aqui")
    button2.paint_image("./res/cell.png")
    button2.pack()
    button2.set_text_position("TOP")
    button3 = Btpy.ButtonIconText(window, 
        "click aqui")
    button3.paint_image("./res/cell.png")
    button3.pack()
    button3.set_text_position("BOTTOM")
    button4 = Btpy.ButtonIconText(window, 
        "click aqui")
    button4.paint_image("./res/cell.png")
    button4.pack()
    button4.set_text_position("RIGHT")
    window.start()

main()