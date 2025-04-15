

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
    button = Btpy.Button(window, "click")
    button.pack()
    button.set_background_color("red")
    button.set_foreground_color("white")
    n = 0
    def fn(e):
        nonlocal n
        button.set_title(f"click {n}")
        n += 1
    button.add_listener(fn)
    btn_enable = Btpy.Button(
        window, "enable")
    btn_enable.pack()
    def fn(e):
        button.enable()
    btn_enable.add_listener(fn)
    btn_disable = Btpy.Button(
        window, "disable")
    btn_disable.pack()
    def fn(e):
        button.disable()
    btn_disable.add_listener(fn)
    window.start()

main()