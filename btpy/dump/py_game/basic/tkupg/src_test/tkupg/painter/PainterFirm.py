



class PainterFirm:

    """
        Clase destinada a la creacion de un componente
        canvas que puede pintarse enviando arrays de imagenes
        que se dibujaran en capas ordenadas.
    """

    # super method
    def __init__(self, window_tk):
        pass

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
        pass

    """
        Funcion que dibuja un array de paint_order_map
        en el canvas.
    """
    # not return
    def draw_paint_order_map_array(self,
            paint_order_map_array):
        pass

    """
        Funcion que dibuja un diccionario
        de paint_order_map.
    """
    def draw_paint_order_map(self, paint_order_map):
        pass

    """
        Funcion que limpia la pantalla de imagenes.
    """
    def clean(self):
        pass

    """
        Funcion que dibuja una image en el
        canvas usando su direccion y locacion.
    """
    def draw_image(self, image_direction, location_x,
            location_y):
        pass

    """
        Funcion que dibuja un punto en el canvas
        usando el punto del puntero, un punto de destino
        y el color del puntero.
    """
    def draw_line(self, point_destiny):
        pass

    """
        Funcion que valida si la direccion de la imagen
        enviada existe.
    """
    # return boolean
    def is_valid_direction(self, direction_image):
        pass

    # ACCESORS ----------------------------------------

    def set_size(self, size_x, size_y):
        pass

    # return int
    def get_size_x(self):
        pass

    # return int
    def get_size_y(self):
        pass

    # return Canvas
    def get_canvas(self):
        pass

    def set_background(self, color_string):
        pass

    """
        Funcion que ajusta un punto en formato int_array
        para el puntero de dibujo.
    """
    def set_point_pointer(self, array):
        pass

    # return int_array
    def get_point_pointer(self):
        pass

    """
        Funcion que ajusta una clave de color
        para el puntero de dibujo.
    """
    def set_pointer_color(self, key):
        pass

    # return string
    def get_pointer_color(self):
        pass
