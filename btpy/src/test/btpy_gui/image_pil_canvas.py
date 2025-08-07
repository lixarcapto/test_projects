

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
from btpy.btpy_images.mod.image_pil_canvas.ImagePilCanvas import ImagePilCanvas
from create_destiny_point import*

def main():
    print("init...")
    r = None
    # -------------------------------------
    

    window = Btpy.Window("title")
    canvas = Btpy.Canvas(window, "canvas")
    canvas.set_size(650, 650)
    canvas.set_background_color("white")
    canvas.pack()
    img_pil = Btpy.create_rgb_image_pil(
        600, 600
    )
    img_canvas = ImagePilCanvas()
    img_canvas.set_image_pil(img_pil)
    img_canvas.set_brush_width(2)
    img_canvas.set_brush_color(
        "red"
    )
    p_list = Btpy.random_point_list(
        20,
        [0, 500]
    )
    img_canvas.draw_point_list_texture(
        p_list,
        "./res/cloud_100x100.png"
    )
    line_list = [[0, 0], [0, 0]]
    for i in range(12):
        line_list = Btpy.create_thunder_shape(
            300,
            300,
            100,
            100,
            30
        )
        img_canvas.draw_line_list(
            line_list)
    canvas.draw_image(
        [0, 0],
        img_canvas.image_pil,
        0
    )
    window.start()


    #---------------------------------
    print(r)

main() 