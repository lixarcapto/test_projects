

from PIL import Image, ImageDraw
from ....btpy_maths.mod.set_point_in_range.set_point_in_range import*

class ImagePilCanvas:

    def __init__(self, image_pil):
        self.image_pil = None
        self.image_draw = None
        self.brush_color_rgb = [0, 0, 0]
        self.brush_with = 1
        self.size_img_list = [0, 0]
        self.set_image_pil(image_pil)

    def set_brush_with(self, SIZE:int):
        self.brush_with = SIZE

    def set_brush_color_rgb(self, 
            RGB_LIST:list[list[int]]):
        self.brush_color_rgb = RGB_LIST

    def set_image_pil(self, image_pil):
        self.image_draw = ImageDraw\
            .Draw(image_pil)
        self.image_pil = image_pil
        self.size_img_list\
            = list(image_pil.size)
        
    def draw_line_list(self, line_list):
        for line in line_list:
            self.draw_line(
                line[0],
                line[1]
            )

    def draw_line(self, 
            POINT_1: list[list[int]], 
            POINT_2: list[list[int]])\
            ->None:
        self.image_draw.line(
            xy=(
                tuple(POINT_1),
                tuple(POINT_2)
            ), 
            fill=tuple(self.brush_color_rgb), 
            width=self.brush_with
        )