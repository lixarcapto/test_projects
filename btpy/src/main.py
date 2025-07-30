

from btpy.Btpy import Btpy
from btpy.btpy_images.mod.image_pil_canvas.ImagePilCanvas import ImagePilCanvas
from create_destiny_point import*
from shader_relampago import*

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
    img_canvas = ImagePilCanvas(img_pil)
    img_canvas.set_brush_with(2)
    img_canvas.set_brush_color_rgb(
        [0, 255, 255]
    )
    line_list = [[0, 0], [0, 0]]
    for i in range(12):
        line_list = shader_relampago(
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