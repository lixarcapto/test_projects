

import sys
import os

# Obtiene el directorio del script actual
current_dir = os.path.dirname(os.path.abspath(__file__))
# Obtiene el directorio padre
parent_dir = os.path.dirname(current_dir)
# Agrega el directorio padre a sys.path
sys.path.append(parent_dir)

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