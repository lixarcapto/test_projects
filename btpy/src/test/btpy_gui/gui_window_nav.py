

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
    window = Btpy.WindowNav("titulo")
    window.set_is_fullscreen(True)
    frame = Btpy.Frame(window)
    btn = Btpy.Button(frame, "frame1")
    btn.grid(0, 0)
    window.add_frame("main", frame)
    frame2 = Btpy.Frame(window)
    btn2 = Btpy.Button(frame2, "frame2")
    btn2.grid(0, 0)
    window.add_frame("second", frame2)
    window.select_frame("main")
    window.start()
    

main()