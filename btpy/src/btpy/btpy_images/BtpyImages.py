

from .in_deps import*
from ..btpy_gui.BtpyGui import BtpyGui

class BtpyImages(BtpyGui):

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
    
    def create_image(self, SIZE_LIST)\
            ->Image:
        return Image.new(
            "RGB", 
            SIZE_LIST, 
            (0, 0, 0, 0)
        )
    
    def matrix_RGB_to_image(
            MATRIX_RGB:list[list])->Image:
        """
        Funcion que convierte una matriz
        Python de listas RGB en un
        formato Image de la libreria
        PIL
        """
        return matrix_RGB_to_Image(
            MATRIX_RGB)
    
    def image_to_matrix_RGB(
            image_pil:Image)\
            ->list[list]:
        return image_to_matrix_RGB(
            image_pil)
    
    def lightens_rgb(RGB_LIST, 
            FACTOR:float=0.1)->list[int]:
        return lightens_rgb(RGB_LIST,
            FACTOR)
    