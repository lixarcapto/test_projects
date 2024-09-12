

from .deps import*

class Painter(WidgetElement):

    """
        Clase destinada a la creacion de un 
        componente canvas que puede pintarse 
        enviando arrays de imagenes que se 
        dibujaran en capas ordenadas.

        PAINT ORDER FIRMA
            Esta es la firma para el envío 
        de diccionarios de tipo Paint order. 
        Los tipos son varios; de momento 
        soporta rutas de imágenes, y lineas.
        Los Paint order se abrevian como POD,
        por paint order dict.
        NOTE: Eliminé el soporte para 
        direcciones separadas para evitar 
        la complejidad innecesaria.

        PO TIPO IMAGE
        po = {
            "type":"image",
            "route":"",
            "point":[0, 0]
        }
        PO TIPO IMAGE LAYOUT
        po = {
            "type":"image_layout",
            "route_array":[],
            "point":[0, 0]
        }
        PO TIPO LINEA
        po = {
            "type":"line",
            "point_1":[0, 0]
            "point_2":[0, 0]
        }
        PO TIPO POLYGON
        po = {
            "type":"polygon",
            "point_array":[]
        }
        PO TIPO TEXT
        po = {
            "type":"text",
            "text":""
        }
    """

    def __init__(self, window_tk):
        self.widget = tkinter.Canvas(
            window_tk.widget)
        self.data = PainterData(self.widget)
        self.init()

    # super method
    def init(self):
        self.set_background(
            self.data.background_color)

    """
    Funcion que dibuja un diccionario
    de paint_order_map.
    """
    def draw_pod_array(self, 
            pod)-> None:
        self.data = draw_pod_array(
            self.data, pod)

    """
    Funcion que dibuja una image en el
    canvas usando su direccion y 
    locacion.
    """
    def draw_image(self, image_direction, 
            location_x, location_y):
        self.data = draw_image(self.data, 
            image_direction, 
            location_x, 
            location_y
        )

    """
    Función envoltorio para el método paint 
    del Canvas tkinter. Esta función no tiene 
    ancho ni color, porque esas son 
    propiedades de la clase painter.
    """
    def draw_line(self, point_ar1, point_ar2):
        self.data = draw_line(self.data, 
            point_ar1, point_ar2)
        
    def draw_line_arr(self, 
            line_arr, 
            fill = "white", 
            width = 1):
        self.data = draw_line_arr(self.data, 
            line_arr, fill, width)
        
    def draw_point(self, point_arr):
        # Dibujar un círculo en el canvas
        DIAMETER:int = 10
        self.widget.create_oval(
            point_arr[0] - DIAMETER, 
            point_arr[1] - DIAMETER, 
            point_arr[0] + DIAMETER, 
            point_arr[1] + DIAMETER, 
            fill= self.data.get_brush_color(),
            width = self.data.get_brush_width())

    def draw_point_list(self, point_list):
        for point in point_list:
            self.draw_point(point)

    """
    Función que dibuja un array de puntos 
    conectados en el canvas.
    """
    def draw_poligon(self, poligon:list[list])\
            -> None:
        self.data = draw_polygon(self.data, 
            poligon)
        
    def repaint(self):
        ancho_actual = self.widget.winfo_width()
        alto_actual = self.widget.winfo_height()
        self.widget.create_rectangle(0, 0,
               ancho_actual,
                alto_actual,
                fill = self.data.background_color)

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

    def draw_rectangle(self, range_location,
            range_size):
        range_extension \
            = left_point_rectangle(
                range_location,
                range_size[0],
                range_size[1]
            )
        self.widget.create_rectangle(
            range_location[0],
            range_location[1],
            range_extension[0],
            range_extension[1],
            fill=self.data.get_brush_color(), 
            width=self.data.get_brush_width()
        )

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

    def get_brush_color(self):
        self.data.get_brush_color()

    def get_brush_with(self):
        return self.data.get_brush_width()
