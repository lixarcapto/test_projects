

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
    
    canvas = Btpy.Canvas(window, "title")
    canvas.pack()
    canvas.set_size(600, 600)
    canvas.draw_image([0, 0],
        "./res/cell.png")
    point_1 = [0, 0]
    point_2 = [300 ,0]
    color = [0, 0, 0]
    for i in range(100):
        canvas.set_brush_color(color)
        canvas.draw_line(point_1, point_2)
        """
        color = Btpy.lightens_rgb(
            color,
            0.08
        )
        """
        point_1[1] += 2
        point_2[1] += 2
    window.start()

main()