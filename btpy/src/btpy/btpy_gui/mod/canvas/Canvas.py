

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
        super().__init__(window)
        # Crear el Canvas
        self.widget = tk.Canvas(
            self.margin, 
            width=400, height=300, 
            bg="white")
        self.widget.pack(
            padx=1, 
            pady=(2, 1)
        )
        self.__buffer_image_list:list = []
        self.__brush_color = "black"
        self.__fill_color = "red"
        self.__guide_color = "red"
        self.__background_color = "white"
        self.__brush_thickness = 3
        self.__guide_thickness = 1
        self.point_cursor = [0, 0]
        self.callback_right_click \
            = (lambda e:e)
        self.callback_left_click \
            = (lambda e:e)
        self.add_default_listener()

    def get_point_cursor(self)->list[int]:
        return self.point_cursor

    def get_height(self)->int:
        return int(self.widget.cget(
            "height"))

    def get_width(self)->int:
        return int(self.widget.cget(
            "width"))

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
    
    def set_guide_color(self, COLOR)->None:
        self.__guide_color = COLOR

    def get_guide_color(self):
        return self.__guide_color
    
    def set_brush_thickness(self, SIZE:int):
        self.__brush_thickness = SIZE

    def get_brush_thickness(self)->int:
        return self.__brush_thickness
    
    def set_guide_thickness(self, SIZE:int):
        self.__guide_thickness = SIZE

    def get_guide_thickness(self)->int:
        return self.__guide_thickness

    def set_brush_color(self, COLOR)->None:
        self.__brush_color = COLOR

    def get_brush_color(self):
        return self.__brush_color

    def set_size(self, WIDTH:int, 
                HEIGHT:int):
        self.widget.config(
            width=WIDTH, height=HEIGHT)

    def draw_line(self, POINT_1:list[int], 
                POINT_2:list[int]):
        self.widget.create_line(
            POINT_1[0], POINT_1[1], 
            POINT_2[0], POINT_2[1], 
            fill=self.__brush_color, 
            width=self.__brush_thickness
        )

    def draw_guide_line(self, 
            POINT_1:list[int], 
            POINT_2:list[int]):
        self.widget.create_line(
            POINT_1[0], POINT_1[1], 
            POINT_2[0], POINT_2[1], 
            fill=self.__guide_color, 
            width=self.__guide_thickness
        )

    def draw_guide_line_x(self, 
            POINT:list[int]):
        p1 = [0, POINT[1]]
        p2 = [self.get_width(), POINT[1]]
        self.draw_guide_line(p1, p2)

    def draw_guide_line_y(self, 
            POINT:list[int]):
        p1 = [POINT[1], 0]
        p2 = [POINT[1], self.get_height()]
        self.draw_guide_line(p1, p2)

    def draw_guide_cross(self, 
            POINT:list[int]):
        self.draw_guide_line_y(POINT)
        self.draw_guide_line_x(POINT)

    def draw_mesh_guide_x(self, 
            DIVISION:int):
        height = self.get_height()
        quotient = height /DIVISION
        y = 2
        while(y < height):
            self.draw_guide_line_x(
                [0, y]
            )
            y += quotient
        self.draw_guide_line_x(
                [0, height]
            )

    def draw_mesh_guide_y(self, 
            DIVISION:int):
        width = self.get_width()
        quotient = width /DIVISION
        x = 2
        while(x < width):
            self.draw_guide_line_y(
                [0, x]
            )
            x += quotient
        self.draw_guide_line_y(
                [0, width]
            )

    def draw_grid_guide(self, DIVISION:int):
        self.draw_mesh_guide_x(DIVISION)
        self.draw_mesh_guide_y(DIVISION)


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

    def draw_image_layers(self, 
            POINT:list[int],
            PATH_LIST:list[str],
            SIZE_LIST:list[int] = [0, 0]):
        for path in PATH_LIST:
            self.draw_image(
                POINT, 
                path,
                SIZE_LIST
            )

    def draw_figure_line(self, 
            LINE_LIST:list[list[list[int]]]):
        for line in LINE_LIST:
            self.draw_line(
                line[0], 
                line[1]
            )

    def draw_cloud_point(self,
            POINT_LIST:list[list[int]]):
        for point in POINT_LIST:
            self.draw_point(point)


    def draw_figure_point(self,
            POINT_LIST:list[list[int]]):
        is_first = True
        point = [0, 0]
        for i in range(len(POINT_LIST) -1):
            self.draw_line(
                POINT_LIST[i], 
                POINT_LIST[i + 1]
            )

    def add_default_listener(self):
        def fn(event):
            self.point_cursor \
                = [event.x, event.y]
            self.callback_right_click(
                event)
        self.widget.bind("<Button-1>", 
            fn)
        def fn(event):
            self.point_cursor \
                = [event.x, event.y]
            self.callback_left_click(
                event)
        self.widget.bind("<Button-3>", 
            fn)

    def add_right_click_listener(self, 
            CALLBACK):
        self.callback_right_click \
            = CALLBACK

    def add_left_click_listener(self, 
            CALLBACK):
        self.callback_left_click \
            = CALLBACK
