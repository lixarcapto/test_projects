

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
import tkinter as tk

def main():
    window = Btpy.Window("titulo")
    window.set_is_fullscreen(True)
    frame = Btpy.FrameSectioned(window)
    frame.pack(True)
    frame.set_margin_color("blue")
    button = Btpy.Button(frame.head, 
                         "button")
    button.pack()
    button2 = Btpy.Button(frame.side_left, 
                         "button")
    button2.pack()
    button3 = Btpy.Button(frame.side_right, 
                         "button")
    button3.pack()
    button4 = Btpy.Button(frame.center, 
                         "button")
    button4.pack()
    button5 = Btpy.Button(frame.feet, 
                         "button")
    button5.pack()
    window.start()

main()