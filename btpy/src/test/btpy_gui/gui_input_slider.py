

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
    button = Btpy.Button(window, "save")
    button.draw_in_direction()
    slider = Btpy.InputSlider(window, 
        True, "volumen")
    slider.set_range([0, 40])
    slider.set_slider_background_color(
        "#FFFFFF"
    )
    slider.set_bar_size(300, 20)
    slider.set_mark_interval(5)
    slider.set_marker_width(50)
    slider.draw_in_direction()
    def fn(e):
        print(slider.get_value())
    button.add_listener(fn)
    window.start()

main()