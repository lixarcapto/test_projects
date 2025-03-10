

from .in_deps import*
from ..btpy_dict.BtpyDict import BtpyDict

class BtpyImages(BtpyDict):

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
    
    def create_png(matriz_rgb, nombre_archivo):
        return create_png(
            matriz_rgb, nombre_archivo)
    
    def matriz_rgb_to_photoimage(matriz_rgb):
        return matriz_rgb_to_photoimage(
            matriz_rgb)
    