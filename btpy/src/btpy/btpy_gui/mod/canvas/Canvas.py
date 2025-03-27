

import tkinter as tk
from ..widget_standard.WidgetStandard import WidgetStandard
from ...mod.create_photo_image.create_photo_image import*

class Canvas(WidgetStandard):

    """
    Este modulo crea un boton de texto
    que detecta eventos por click en su 
    area para ejecutar una funcion callback.
    """

    def __init__(self, window, text = ""):
        super().__init__()
        # Crear el Canvas
        self.widget = tk.Canvas(
            window.widget, 
            width=400, height=300, 
            bg="white")
        self.__buffer_image_list:list = []
        self.__brush_color = "black"
        self.__fill_color = "red"
        self.__background_color = "white"
        self.__brush_thickness = 3

    def get_height(self):
        return self.widget.cget("height")

    def get_width(self):
        return self.widget.cget("width")

    def repaint(self):
        self.widget.delete("all")
        self.__buffer_image_list = []

    def set_background_color(self, COLOR)\
            ->None:
        super().set_background_color(COLOR)
        self.__background_color = COLOR

    def get_background_color(self):
        return self.__background_color

    def set_fill_color(self, COLOR)->None:
        self.__fill_color = COLOR

    def get_fill_color(self):
        return self.__fill_color

    def set_brush_color(self, COLOR)->None:
        self.__brush_color = COLOR

    def get_brush_color(self):
        return self.__brush_color
        
    def pack(self, MARGIN:int = 0):
        self.widget.pack()

    def set_size(self, WIDTH:int, 
                HEIGHT:int):
        self.widget.config(
            width=WIDTH, height=HEIGHT)

    def draw_line(self, POINT_1, 
                POINT_2):
        self.widget.create_line(
            POINT_1[0], POINT_1[1], 
            POINT_2[0], POINT_2[1], 
            fill=self.__brush_color, 
            width=self.__brush_thickness
        )

    def draw_circle(self, POINT:list[int], 
            DIAMETER:int):
        self.widget.create_oval(
            POINT[0] + self.__brush_thickness, 
            POINT[1] + self.__brush_thickness, 
            DIAMETER, DIAMETER, 
            fill=self.__fill_color, 
            outline=self.__brush_color, 
            width=self.__brush_thickness
        )

    def draw_point(self, POINT:list[int]):
        self.widget.create_oval(
            POINT[0], 
            POINT[1], 
            POINT[0] + self.__brush_thickness, 
            POINT[1] + self.__brush_thickness, 
            fill=self.__brush_color, 
            outline=self.__brush_color, 
            width=self.__brush_thickness
        )

    def draw_rectangle(self, POINT, 
            WIDTH:int, HEIGHT:int):
        self.widget.create_rectangle(
            POINT[0], POINT[1], 
            POINT[0] + WIDTH, 
            POINT[1] + HEIGHT, 
            fill=self.__fill_color, 
            outline=self.__brush_color, 
            width=self.__brush_thickness
        )

    def draw_image(self, POINT:list[int], 
            PATH:str, SIZE_LIST:list[int]
                = [0, 0]):
        photo_image = create_photo_image(
            PATH, SIZE_LIST
        )
        self.__buffer_image_list.append(
            photo_image)
        self.widget.create_image(
            POINT[0], POINT[1], 
            image=photo_image
        )