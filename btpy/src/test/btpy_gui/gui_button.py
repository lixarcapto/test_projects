

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
    button.draw_in_direction()
    button.set_background_color("#FF0000")
    button.set_font_color("#FFFFFF")
    n = 0
    def fn(e):
        nonlocal n
        button.set_title(f"click {n}")
        n += 1
    button.add_listener(fn)
    btn_enable = Btpy.Button(
        window, "enable")
    btn_enable.draw_in_direction()
    def fn(e):
        button.enable()
    btn_enable.add_listener(fn)
    btn_disable = Btpy.Button(
        window, "disable")
    btn_disable.draw_in_direction()
    def fn(e):
        button.disable()
    btn_disable.add_listener(fn)
    window.start()

main()