


class PainterData:

    def __init__(self, canvas_widget) -> None:
        self.widget = canvas_widget
        # ultima posicion de la brocha
        self.__brush_point = [0, 0]
        self.__brush_width= 1
        self.__brush_color = "white"
        # buffer de imagenes cargadas
        self.__buffer_image_arr = []
        

    def set_brush_point(self, point)->None:
        self.__brush_point = point

    def get_brush_point(self):
        return self.__brush_point
    
    def set_brush_width(self, number)->None:
        self.__brush_width = number

    def get_brush_width(self):
        return self.__brush_width
    
    def set_brush_color(self, color:str)->None:
        self.__brush_color = color

    def get_brush_color(self):
        return self.__brush_color
    
    """
    Función que carga imágenes en el buffer;
    para evitar que el manejador de memoria 
    las borre.
    """
    def add_image_buffer(self, image)->None:
        self.__buffer_image_arr.append(image)

    """
    Función que borra todas las imágenes 
    cargadas del buffer image.
    """
    def clean_image_buffer(self)->None:
        self.__buffer_image_arr.clear()