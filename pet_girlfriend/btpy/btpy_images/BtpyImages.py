

from .in_deps import*
from ..btpy_gui_2.BtpyGui2 import BtpyGui2

class BtpyImages(BtpyGui2):

    """
    Modulo statico de herramientas 
    para trabajar con matrizes RGB.
    """

    def save_numpy_rgb_as_PNG(
            numpy_image_RGB, name:str)->None:
        return save_numpy_rgb_as_PNG(
            numpy_image_RGB, name)
    
    def create_matrix_rgb(filas, columnas):
        return create_matrix_rgb(
            filas, columnas)
    
    def create_png(matriz_rgb, 
            nombre_archivo):
        return create_png(
            matriz_rgb, nombre_archivo)
    
    def matrix_rgb_to_photoimage(
            matriz_rgb):
        return matriz_rgb_to_photoimage(
            matriz_rgb)

    def image_to_photo_image( 
            image_pil:Image)\
            ->tk.PhotoImage:
        # Convertir la imagen PIL a 
        # PhotoImage
        return ImageTk.PhotoImage(
            image_pil)
    
    def matrix_rgb_to_image_pil(
            MATRIX_RGB:list[list])->Image:
        """
        Funcion que convierte una matriz
        Python de listas RGB en un
        formato Image de la libreria
        PIL
        """
        return matrix_rgb_to_image_pil(
            MATRIX_RGB)
    
    def image_pil_to_matrix_RGB(
            image_pil:Image)\
            ->list[list]:
        return image_pil_to_matrix_RGB(
            image_pil)
    
    def lightens_rgb(RGB_LIST, 
            FACTOR:float=0.1)->list[int]:
        return lightens_rgb(RGB_LIST,
            FACTOR)
    
    def create_rgb_image_pil(WIDTH, HEIGHT)\
            ->Image:
        return create_rgb_image_pil(
                WIDTH, HEIGHT)
    
    def create_rgba_image_pil(WIDTH, 
            HEIGHT)\
            ->Image:
        return create_rgba_image_pil(
                WIDTH, HEIGHT)

    def blacken_rgb(RGB_LIST:list[int], 
            FACTOR:float = 0.1)->list[int]:
        """
        Oscurece un color RGB.
        Args:
        color_rgb: Una tupla o lista 
        de 3 elementos que representa 
        un color RGB (R, G, B), donde 
        los valores están en el rango 
        de 0 a 255.
        factor: Un valor flotante entre 
        0 y 1 que determina cuánto se 
        va a oscurecer el color.
        0 no cambia el color, 1 lo 
        oscurece completamente a negro. 
        El valor por defecto es 0.1.
        Returns:
        Una tupla de 3 elementos que 
        representa el color RGB oscurecido.
        """
        return blacken_rgb(
            RGB_LIST, FACTOR)
    
    def image_pil_to_binary(
            imagen_pil: Image.Image, 
            formato: str = "PNG")\
            -> bytes | None:
        """
        Convierte un objeto de imagen PIL 
        (Pillow) a una secuencia de bytes 
        binarios.
        imagen_pil (Image.Image): El objeto 
        de imagen de Pillow.
        formato (str): 
            * "PNG" 
            * "JPEG"
            * "BMP"
        Debe ser un formato soportado 
        por Pillow. Por defecto es "PNG".
        """
        return image_pil_to_binary(
            imagen_pil,
            formato
        )
    
    def binary_to_image_pil(
            contenido_binario: bytes)\
            -> Image.Image | None:
        """
        Convierte una secuencia de bytes 
        binarios a un objeto de imagen PIL.
        """
        return binary_to_image_pil(
            contenido_binario
        )
    
    def write_image_pil_as_png(
            IMAGE_PIL: Image.Image, 
            PATH: str) -> bool:
        """
        Guarda un objeto de imagen PIL 
        (Pillow) como un archivo PNG.
        """
        return write_image_pil_as_png(
            IMAGE_PIL,
            PATH
        )
    
    def read_image_as_image_pil(
            PATH: str)\
            -> Image.Image | None:
        """
        Lee un archivo de imagen (
        JPG, PNG, BMP, etc.) y lo 
        convierte en un objeto PIL.Image.
        """
        return read_image_as_image_pil(
            PATH
        )
    