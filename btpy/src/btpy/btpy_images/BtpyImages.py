

from .in_deps import*
from .mod.create_matrix_rgb import*
from .mod.create_png import*
from .mod.matrix_rgb_to_photoimage import*
from ..btpy_engine.BtpyEngine import BtpyEngine

class BtpyImages(BtpyEngine):

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
    