

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
    color = [255, 255, 255]
    canvas = Btpy.Canvas(window, "canvas")
    canvas.draw_in_direction()
    canvas.set_size(300, 300)
    point = [300, 0]
    for i in range(100):
        canvas.draw_line([0, 0], point)
        canvas.set_brush_color(color)
        point[1] += 3
        color = Btpy.blacken_rgb(
            color, 0.01)
    window.start()

main()