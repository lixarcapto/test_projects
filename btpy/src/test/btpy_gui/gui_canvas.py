

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
    canvas.draw_path_image([0, 0],
        "./res/cell.png")
    point_1 = [0, 0]
    point_2 = [300 ,0]
    canvas_2 = Btpy.Canvas(
        window, "copy")
    canvas_2.pack()
    for i in range(5):
        canvas.set_brush_color("green")
        canvas.draw_line(point_1, point_2)
        canvas.set_brush_color("blue")
        canvas.draw_circle([40, 40], 150)
        point_1[1] += 2
        point_2[1] += 2
    image = canvas.get_image_reflection()
    canvas_2.draw_image([0, 0], image)
    window.start()

main()