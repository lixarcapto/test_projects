

from .dependences import*
from .dependences import CanvasAdapter

class Painter(PainterFirm):

    """
        Clase destinada a la creacion de un componente
        canvas que puede pintarse enviando arrays de imagenes
        que se dibujaran en capas ordenadas.
    """

    def __init__(self, window_tk):
        self.__canvas = CanvasAdapter(window_tk)
        self.__point_pointer = [0, 0]
        self.__photo_image_array = []
        self.__color_pointer = "black"
        self.set_size(1200, 700)
        self.set_background("black")
        self.init()

    # super method
    def init(self):
        self.__canvas.pack()

    """
    Funcion que dibuja un array de diccionarios de tipo
    paint order map.
    El paint order map es:
        paint_order = {
        "image_names_array" : [],
        "direction": "",
        "format": "",
        "location_x" : "0",
        "location_y" : "0"
        }
    """

    """
        Funcion que genera una direccion de imagen
        completa a partir de un diccionario
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
        Funcion que dibuja un array de paint_order_map
        en el canvas.
    """
    # not return
    def draw_paint_order_map_array(self,
            paint_order_map_array):
        #photo_image = PhotoImage(file = "./files/cazacarro.png")
        self.__photo_image_array.clear()
        for pom in paint_order_map_array:
            self.draw_paint_order_map(pom)

    """
        Funcion que dibuja un diccionario
        de paint_order_map.
    """
    def draw_paint_order_map(self, paint_order_map):
        pom = paint_order_map
        direction_image_array = self\
            .create_route_array_from_paint_order_map(\
            pom)
        # crea las direcciones
        for i in range(len(direction_image_array)):
            self.draw_image(\
                direction_image_array[i],
                int(pom["location_x"]),
                int(pom["location_y"])
                )

    def clean(self):
        self.__photo_image_array.clear()

    """
        Funcion que dibuja una image en el
        canvas usando su direccion y locacion.
    """
    def draw_image(self, image_direction, location_x,
            location_y):
        # si la direccion no es valida salta al siguiente
        if(not self.is_valid_direction(image_direction)):
            return None
        # carga un photo image y lo almacena
        photo_image = PhotoImage(file = image_direction)
        self.__photo_image_array.append(photo_image)
        # dibuja el photo_image
        self.__canvas.create_image(\
            location_x,
            location_y,
            photo_image,
            "nw"
        )

    def draw_line(self, point_destiny):
        point_pointer = self.get_point_pointer()
        self.__canvas.create_line(
            point_pointer[0],
            point_pointer[1],
            point_destiny[0],
            point_destiny[1],
            self.get_pointer_color()
        )

    """
        Funcion que valida si la direccion de la imagen
        enviada existe.
    """
    # return boolean
    def is_valid_direction(self, direction_image):
        if (not os.path.exists(direction_image)):
            text = write_error(\
                error = "direccion invalida",
                file_name = "Painter",
                function_name = "draw_paint_order_map",
                data_error = direction_image
                )
            print(text)
            return False
        return True

    # ACCESORS ----------------------------------------

    def set_size(self, size_x, size_y):
        self.__width = size_x
        self.__height = size_y
        self.__canvas.set_size( \
            self.__width,
            self.__height
        )

    # return int
    def get_size_x(self):
        return self.__width

    # return int
    def get_size_y(self):
        return self.__height

    # return Canvas
    def get_canvas(self):
        return self.__canvas

    def set_background(self, color_string):
        self.__canvas.set_background(color_string)
        self.__background_color = color_string

    def set_point_pointer(self, array):
        self.__point_pointer = array

    # return int_array
    def get_point_pointer(self):
        return self.__point_pointer

    def set_pointer_color(self, key):
        self.__color_pointer = key

    # return string
    def get_pointer_color(self):
        return self.__color_pointer
