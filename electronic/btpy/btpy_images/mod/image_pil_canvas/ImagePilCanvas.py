

from PIL import Image, ImageDraw
from ....btpy_maths.mod.set_point_in_range.set_point_in_range import*
from btpy.Btpy import Btpy
from ....btpy_images.mod.create_image_pil.create_image_pil import*

from PIL import Image
import os

class ImagePilCanvas:

    """
    Esta clase permite modificar imagenes
    de una forma mas facil y rapida.
    Es un wrapper de image pil draw.
    """

    def __init__(self):
        self.image_pil:Image = None
        self.image_draw = None
        self.brush_color_rgb\
            :list[list[int]] = [0, 0, 0]
        self.__brush_width = 1
        self.brush_border_color = [0, 0, 0]
        self.size_img_list = [0, 0]

    def get_brush_width(self)->int:
        """
        return the brush width
        """
        return self.__brush_width

    def set_brush_width(self, SIZE:int):
        self.__brush_width = SIZE

    def set_brush_color(self, 
            COLOR_ANY:any):
        color = Btpy.adapt_rgb(COLOR_ANY)
        self.brush_color_rgb = color

    def set_brush_border_color(self, 
            COLOR_ANY:any):
        color = Btpy.adapt_rgb(COLOR_ANY)
        self.brush_border_color = color

    def new_image_pil(self, 
            WIDTH:int, HEIGHT:int):
        self.image_pil = create_rgb_image_pil(
            WIDTH, 
            HEIGHT
        )

    def set_image_pil(self, 
            image_pil:Image):
        self.image_draw = ImageDraw\
            .Draw(image_pil)
        self.image_pil = image_pil
        self.size_img_list\
            = list(image_pil.size)
        
    def get_image_pil(self)->Image:
        return self.image_pil
        
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
            width=self.__brush_width
        )

    def draw_point_list(self, 
            POINT_LIST):
        for point in POINT_LIST:
            self.draw_point(point)

    def draw_image(self,
            image_pil: Image.Image,
            posicion: tuple[int, int],
            usar_mascara: bool = True
            ) -> Image.Image:
        # Si la imagen a pegar no tiene un canal alfa, la convertimos a RGBA.
        # Esto asegura que podemos obtener una máscara de transparencia.
        if image_pil.mode != 'RGBA':
            image_pil = image_pil.convert('RGBA')
    
        # Separamos los canales de la imagen a pegar para obtener el canal alfa (transparencia)
        _, _, _, a = image_pil.split()

        try:
            # Pegamos la imagen en el lienzo, usando su propio canal alfa como máscara.
            # Esto previene que los píxeles transparentes de 'imagen_a_pegar'
            # sobrescriban los píxeles de 'imagen_base'.
            self.image_pil.paste(
                image_pil, 
                posicion, 
                mask=a
            )
        except ValueError as e:
            print(f"❌ Error al pegar la imagen: {e}. Verifique que las coordenadas y las dimensiones sean correctas.")

    def draw_point_list_texture(self, 
            POINT_LIST, IMAGE_TEXTURE):
        image = None
        if(isinstance(IMAGE_TEXTURE, str)):
            image = Btpy.read_image_as_image_pil(
                IMAGE_TEXTURE
            )
        else:
            image = IMAGE_TEXTURE
        for point in POINT_LIST:
            self.draw_image(
                image,
                point,
                True
            )

    def draw_point(self, POINT):
        """
        Dibuja un círculo en un objeto de imagen PIL.

        Args:
        imagen_pil (Image.Image): El objeto de imagen de Pillow sobre el que se dibujará.
                                  Se crea una copia para no modificar la original.
        centro_x (int): La coordenada X del centro del círculo.
        centro_y (int): La coordenada Y del centro del círculo.
        radio (int): El radio del círculo en píxeles.
        color_rgb (tuple[int, int, int]): Una tupla de 3 enteros (R, G, B) para el color del círculo.
                                          Si ancho_borde es 0, este es el color de relleno.
        ancho_borde (int): El grosor del borde del círculo en píxeles.
                           Si es 0 (por defecto), el círculo será sólido.

        Returns:
        Image.Image: Una nueva imagen PIL con el círculo dibujado.
        """
        # Calcular las coordenadas de la caja delimitadora (bounding box)
        # La caja va desde (centro_x - radio, centro_y - radio) hasta (centro_x + radio, centro_y + radio)
        radio = self.__brush_width / 2
        centro_x: int = POINT[0]
        centro_y: int = POINT[1]
        x1 = centro_x - radio
        y1 = centro_y - radio
        x2 = centro_x + radio
        y2 = centro_y + radio
        
        # El método ellipse() necesita la caja delimitadora como una tupla: (x1, y1, x2, y2)
        caja_delimitadora = (x1, y1, x2, y2)

        # fill=None significa que no hay relleno interior.
        # fill=color_rgb rellenaría el círculo con el mismo color del borde.
        self.image_draw.ellipse(
            xy=caja_delimitadora, 
            outline=tuple(self.brush_color_rgb), 
            width=self.__brush_width, 
            fill=tuple(self.brush_color_rgb)
        )

    def draw_circle(
        self,
        POINT,
        DIAMETER: int
        ):
        """
        Dibuja un círculo en un objeto de imagen PIL.

        Args:
        imagen_pil (Image.Image): El objeto de imagen de Pillow sobre el que se dibujará.
                                  Se crea una copia para no modificar la original.
        centro_x (int): La coordenada X del centro del círculo.
        centro_y (int): La coordenada Y del centro del círculo.
        radio (int): El radio del círculo en píxeles.
        color_rgb (tuple[int, int, int]): Una tupla de 3 enteros (R, G, B) para el color del círculo.
                                          Si ancho_borde es 0, este es el color de relleno.
        ancho_borde (int): El grosor del borde del círculo en píxeles.
                           Si es 0 (por defecto), el círculo será sólido.

        Returns:
        Image.Image: Una nueva imagen PIL con el círculo dibujado.
        """
        # Calcular las coordenadas de la caja delimitadora (bounding box)
        # La caja va desde (centro_x - radio, centro_y - radio) hasta (centro_x + radio, centro_y + radio)
        radio = DIAMETER / 2
        centro_x: int = POINT[0]
        centro_y: int = POINT[1]
        x1 = centro_x - radio
        y1 = centro_y - radio
        x2 = centro_x + radio
        y2 = centro_y + radio
        
        # El método ellipse() necesita la caja delimitadora como una tupla: (x1, y1, x2, y2)
        caja_delimitadora = (x1, y1, x2, y2)

        # fill=None significa que no hay relleno interior.
        # fill=color_rgb rellenaría el círculo con el mismo color del borde.
        self.image_draw.ellipse(
            xy=caja_delimitadora, 
            outline=tuple(self.brush_border_color), 
            width=self.__brush_width, 
            fill=tuple(self.brush_color_rgb)
        )
