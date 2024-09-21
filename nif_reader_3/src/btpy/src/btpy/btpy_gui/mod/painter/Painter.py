

import os
from ..WidgetElement import WidgetElement
import tkinter
from tkinter import PhotoImage
from ....btpy_persistence.mod\
    .check_path.check_path import*
from ....btpy_maths.mod.vector_sum.vector_sum import*

class Painter(WidgetElement):

    """
     Widget especializado que mejora 
     funcionalidades del Canvas de la 
     librería de Tkinter.  añade 
     funciones para el pintado avanzadas, 
     como imagenes en capas,  dibujar 
     poligonos, puntos y nuevas  
     opciones para cuadrados.
    """

    def __init__(self, widget):
        super().__init__()
        self.widget = tkinter.Canvas(
           widget)
        self.__background_color = "black"
        self.__brush_width = 1
        self.__font = ("Arial", 14)
        self.__font_color = "white"
        self.__brush_color = "red"
        self.__brush_point = [0, 0]
        # buffer de imagenes cargadas
        self.__buffer_image_arr = []

    # ACCESSORS -----------------------------

    def set_font(self, NAME_FONT, SIZE):
        self.__font = [NAME_FONT, SIZE]

    def set_font_color(self, COLOR):
        self.__font_color = COLOR

    def set_brush_width(self, WIDTH:int):
        self.__brush_width = WIDTH

    def get_font_color(self):
        return self.__font_color

    def get_brush_width(self)->int:
        return self.__brush_width

    def set_brush_color(self, COLOR:str|list):
        self.__brush_color = COLOR

    def get_brush_color(self)->str|list:
        return self.__brush_color
    
    def set_background_color(self, COLOR:str|list):
        self.__background_color = COLOR

    def get_background_color(self)->str|list:
        return self.__background_color
    
    def set_brush_point(self, 
            POINT:list[int|float]):
        self.__brush_point = POINT

    def get_brush_point(self):
        return self.__brush_point

    # MUTATORS --------------------------------

    # LISTENERS

    def right_click_listener(self, 
            callback):
        self.widget.bind(
            "<Button-3>", callback
        )

    def center_click_listener(self, 
            callback):
        self.widget.bind(
            "<Button-2>", callback
        )

    def left_click_listener(self, 
            callback):
        self.widget.bind(
            "<Button-1>", callback
        )

    def mouse_move_listener(self, 
            callback):
        self.widget.bind(
            "<Motion>", callback
        )

    def mouse_enter_listener(self, 
            callback):
        self.widget.bind(
            "<Enter>", callback
        )

    def leave_enter_listener(self, 
            callback):
        self.widget.bind(
            "<Leave>", callback
        )

    # ...

    def repaint(self)->None:
        """
        Funcion que repinta todo el canvas
        con el color de backgrond
        """
        width = self.widget.winfo_width()
        height = self.widget.winfo_height()
        self.widget.create_rectangle(
            0, 0,
            width,
            height,
            fill = self.__background_color
        )

    def __free_buffer_image(self):
        self.__buffer_image_arr.clear()

    def draw_image(self, ROUTE:str, 
            POINT_ARR:list[int|float],
            FORMAT = ".png",)->None:
        """
        Funcion que dibuja una image en el
        canvas usando su direccion y locacion.
        """
        # si la direccion no es valida 
        # salta al siguiente
        if(not check_path(ROUTE, FORMAT)):
            print(f"ERROR: invalid route {ROUTE}")
        # carga un photo image y lo almacena
        photo_image = PhotoImage(
            file= ROUTE)
        self.__buffer_image_arr.append(
            photo_image)
        # dibuja el photo_image
        self.widget.create_image(\
            POINT_ARR[1],
            POINT_ARR[0],
            image =photo_image,
            anchor="nw"
        )

    def draw_text(self, TEXT,
            POINT:list[int|float]):
        y_mod = self.__font[1]
        x_mod = (self.__font[1] * len(TEXT)) / 2
        f_point = vector_sum(
            POINT, 
            [x_mod, y_mod])
        self.widget.create_text(
            f_point[0], f_point[1], 
            text=TEXT,
            font=self.__font,
            fill= self.__font_color
        )

    def draw_image_layout(self, 
            IMAGE_LAYOUT:list[str], 
            POINT:list[int|float])->None:
        for route in IMAGE_LAYOUT:
            self.draw_image(\
                route,
                [int(POINT[0]), 
                 int(POINT[1])]
            )

    def draw_circle(self, 
            RADIUS_POINT, MID_POINT):
        self.widget.create_oval(
            MID_POINT[0], MID_POINT[1], 
            RADIUS_POINT[0], RADIUS_POINT[1], 
            fill=self.__brush_color,
            width=self.__brush_width
        )
    
    def draw_line(self, POINT_1, POINT_2):
        """
        Función envoltorio para el método paint 
        del Canvas tkinter.
        """
        self.widget.create_line(
            POINT_1[0],
            POINT_1[1],
            POINT_2[0],
            POINT_2[1],
            fill= self.__brush_color, 
            width= self.__brush_width
        )

    def draw_line_arr(self, 
            LINE_ARR:list[list]):
        """
        Función envoltorio para el método 
        paint del Canvas tkinter. Esta 
        función no tiene ancho ni color, 
        porque esas son propiedades de la 
        clase painter.
        """
        point_1 = 0
        point_2 = 0
        for line in LINE_ARR:
            point_1 = line[0]
            point_2 = line[1]
            self.widget.create_line(
                point_1[0],
                point_1[1],
                point_2[0],
                point_2[1],
                fill= self.__brush_color, 
                width= self.__brush_width
            )

    def draw_point_list(self, POINT_ARR):
        # Dibujar un círculo en el canvas
        DIAMETER:int = 10
        self.widget.create_oval(
            POINT_ARR[0] - DIAMETER, 
            POINT_ARR[1] - DIAMETER, 
            POINT_ARR[0] + DIAMETER, 
            POINT_ARR[1] + DIAMETER, 
            fill= self.__brush_color,
            width = self.__brush_width
        )

    def draw_polygon(self, 
            POINT_ARR:list[list])\
            -> None:
        """
        Función que dibuja un array de 
        puntos conectados en el canvas.
        """
        final_point = [0, 0]
        is_first = True
        for point_ar in POINT_ARR:
            if(is_first):
                is_first = False
            else:
                self.draw_line(
                    point_ar,
                    final_point
                )
            final_point = point_ar

    
    def traze_line(self, 
            POINT_DESTINY:list[int])->None:
        """
        Función que traza una línea desde 
        el  puntero dónde se encuentra 
        actualmente la brocha.
        """
        self.widget.create_line(
            self.__brush_point[0],
            self.__brush_point[1],
            POINT_DESTINY[0],
            POINT_DESTINY[1],
            fill=self.__brush_color, 
            width=self.__brush_width
        )
        self.__brush_point = POINT_DESTINY

    def draw_rectangle(self, 
            POINT_ORIGEN:list[int|float],
            POINT_EXTENSION:list[int|float]):
        self.widget.create_rectangle(
            POINT_ORIGEN[0],
            POINT_ORIGEN[1],
            POINT_EXTENSION[0],
            POINT_EXTENSION[1],
            fill=self.__brush_color, 
            width=self.__brush_width
        )

    def draw_image_dict(self, IMAGE_DICT):
        """
        {"route", "point"}
        """
        self.draw_image(
            IMAGE_DICT["route"],
            IMAGE_DICT["point"],
            ".png"
        )

    def draw_image_layout_dict(self, 
            IMAGE_LAYOUT_DICT)->None:
        """
        {"route_array", "point"}
        """
        point = IMAGE_LAYOUT_DICT["point"]
        route_arr = IMAGE_LAYOUT_DICT["route_array"]
        for route in route_arr:
            self.draw_image(\
                route,
                point,
                ".png"
            )

    def draw_image_layout_dict_array(self,
            image_layout_dict_array):
        for e in image_layout_dict_array:
            self.draw_image_layout_dict(e)

    def draw_rectangle_by_size(self,
            LOCATION_POINT, SIZE_X,
            SIZE_Y):
        """
        Funcion que dibuja un rectangulo
        a partir de su origen y tamaño
        """
        destiny1 = vector_sum(
            LOCATION_POINT, 
            [SIZE_X, SIZE_Y])
        self.draw_rectangle(
            LOCATION_POINT,
            destiny1
        )

    def draw_label_text(self,
            TEXT, LOCATION_POINT):
        """
        Funcion que dibuja una etiqueta
        con un texto en su interior.
        """
        leng = len(TEXT)
        # calcula el tamaño x del texto
        rect_size_x = leng * self.__font[1]
        # calcula la mitad de la fuente
        mid_font_size = round(
            self.__font[1] / 2)
        # calcula el tamaño y del texto
        rect_size_y = mid_font_size\
            + mid_font_size\
            + self.__font[1]
        # dibuja el rectangulo
        self.draw_rectangle_by_size(
            LOCATION_POINT,
            rect_size_x,
            rect_size_y
        )
        # dibuja el texto
        self.draw_text(TEXT, 
            LOCATION_POINT)

    def draw_polygon_dict(self, 
            POLYGON_DICT):
        """
        {"point_array"}
        """
        self.draw_polygon(
            POLYGON_DICT["point_array"]
        )
        
    def draw_line_arr_dict(self, LINE_ARR):
        """
        {"line_array"}
        """
        self.draw_line_arr(
            LINE_ARR["line_array"]
        )

    # PRIVATE ---------------------------------