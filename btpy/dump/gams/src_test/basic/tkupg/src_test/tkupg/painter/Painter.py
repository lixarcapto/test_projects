

from .deps import*
from ..WidgetElement import WidgetElement
import tkinter
from .create_paint_order import*
from .PainterData import PainterData

class Painter(WidgetElement):

    """
        Clase destinada a la creacion de un 
        componente canvas que puede pintarse 
        enviando arrays de imagenes que se 
        dibujaran en capas ordenadas.
    """

    def __init__(self, window_tk):
        self.widget = tkinter.Canvas(
            window_tk.widget)
        self.data = PainterData(self.widget)
        self.init()

    # super method
    def init(self):
        self.set_background("black")

    """
    Funcion que genera una direccion de 
    imagen completa a partir de un diccionario
    paint_order_map.
    """
    # return string_array
    def create_route_array_from_paint_order_map(\
            self, paint_order_map):
        image_direction_array = []
        route = ""
        names_array = paint_order_map["image_names_array"]
        for i in range(len(names_array)):
            route = ""
            route += paint_order_map["direction"]
            route += names_array[i]
            route += paint_order_map["format"]
            image_direction_array.append(route)
        return image_direction_array
    
    """
    Función que recompone rutas descompuestas
    a imágenes a rutas completas.
    """
    # return string_array
    def recompose_routes(self, route:str, 
            names_arr:list[str], format:str)\
            -> list[str]:
        complete_route_arr = []
        full_route = ""
        for i in range(len(names_arr)):
            full_route = ""
            full_route += route
            full_route += names_arr[i]
            full_route += format
            complete_route_arr.append(route)
        return complete_route_arr

    """
        Funcion que dibuja un array de 
        paint_order en el canvas.
    """
    # not return
    def draw_paint_order_map_array(self,
            paint_order_map_array):
        #photo_image = PhotoImage(file = "./files/cazacarro.png")
        self.data.clean_image_buffer()
        for po in paint_order_map_array:
            self.draw_paint_order(po)

    def draw_paint_order_image(self, 
        paint_order):
        po = paint_order
        # recompone las direcciones
        routes_arr = self.recompose_routes(
            po["direction"],
            po["image_names_array"],
            po["format"]
        )
        # dibuja las imagenes
        for i in range(len(routes_arr)):
            self.draw_image(\
                routes_arr[i],
                int(po["point_location"][0]),
                int(po["point_location"][1])
                )
            
    def draw_paint_order_polygon(self,
            paint_order):
        po = paint_order
        self.set_brush_width(po["width"])
        self.set_brush_width(po["color_key"])
        self.draw_poligon(po["poligon"])

    """
    Funcion que dibuja un diccionario
    de paint_order_map.
    """
    def draw_paint_order(self, 
                paint_order):
        po = paint_order
        if(po["paint_order"] == "image"):
            self.draw_paint_order_image(po)
        elif(po["paint_order"] == "poligon"):
            self.draw_paint_order_poligon(po)

    """
        Funcion que dibuja una image en el
        canvas usando su direccion y locacion.
    """
    def draw_image(self, image_direction, 
            location_x, location_y):
        # si la direccion no es valida 
        # salta al siguiente
        if(not self.is_valid_direction(image_direction)):
            return None
        # carga un photo image y lo almacena
        photo_image = PhotoImage(
            file = image_direction)
        self.add_in_buffer(photo_image)
        # dibuja el photo_image
        self.widget.create_image(\
            location_x,
            location_y,
            photo_image,
            "nw"
        )

    """
    Función envoltorio para el método paint 
    del Canvas tkinter. Esta función no tiene 
    ancho ni color, porque esas son 
    propiedades de la clase painter.
    """
    def draw_line(self, point_ar1, point_ar2):
        self.widget.create_line(
            point_ar1[0],
            point_ar1[1],
            point_ar2[0],
            point_ar2[1],
            fill=self.data.get_brush_color(), 
            width=self.data.get_brush_width()
        )

    """
    Función que dibuja un array de puntos 
    conectados en el canvas.
    """
    def draw_poligon(self, poligon:list[list])\
            -> None:
        last_point = [0, 0]
        is_first = True
        for point_ar in poligon:
            if(is_first):
                is_first = False
                continue
            self.draw_line(
                point_ar,
                last_point
            )
            last_point = point_ar

    """
    Función que traza una línea desde el 
    puntero dónde se encuentra actualmente 
    la brocha.
    """
    def traze_line(self, 
            point_destiny:list[int])->None:
        point_pointer = self.get_point_pointer()
        self.widget.create_line(
            point_pointer[0],
            point_pointer[1],
            point_destiny[0],
            point_destiny[1],
            fill=self.data.get_brush_color(), 
            width=self.data.get_brush_width()
        )

    """
        Funcion que valida si la direccion de la imagen
        enviada existe.
    """
    # return boolean
    def is_valid_direction(self, direction_image):
        if (not os.path.exists(direction_image)):
            r = f"direccion invalida ({direction_image})"
            raise Exception(r)
        return True

    def draw_rectangle(self, range_location,
            range_size):
        range_extension = self \
            .calcule_left_point_rectangle(
                range_location,
                range_size
            )
        self.widget.create_rectangle(
            range_location[0],
            range_location[1],
            range_extension[0],
            range_extension[1],
            fill=self.data.get_brush_color(), 
            width=self.data.get_brush_width()
        )

    def calcule_left_point_rectangle(self,
            range_location, range_size):
        height = range_size[1]
        width = range_size[0]
        top_right_y = range_location[0]
        top_right_x = range_location[1]
        bottom_left_x = top_right_x + width
        # Calculate bottom-left x-coordinate
        bottom_left_y = top_right_y + height
        # Calculate bottom-left y-coordinate
        point_ar = [bottom_left_y, bottom_left_x]
        return point_ar

    # ACCESORS ----------------------------------------
    
    def set_brush_point(self, point_ar):
        self.data.set_brush_point(point_ar)

    def set_brush_color(self, key_color):
        self.data.set_brush_color(key_color)

    def set_brush_width(self, integer):
        self.data.set_brush_width(integer)

    # return int_array
    def get_brush_point(self):
        return self.data.get_brush_point()

    def get_brush_color(self, key_color):
        self.data.get_brush_color()

    def get_brush_with(self):
        return self.data.get_brush_width()
