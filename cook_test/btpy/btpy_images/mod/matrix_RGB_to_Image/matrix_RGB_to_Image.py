

from PIL import Image
import numpy as np

def matrix_RGB_to_Image(
        MATRIX_RGB:list[list])->Image:
    """
    Funcion que convierte una matriz
    Python de listas RGB en un
    formato Image de la libreria
    PIL
    """
    # Convertir la lista de listas a un 
    # array NumPy (opcional, pero mejora 
    # el rendimiento)
    matriz_np = np.array(MATRIX_RGB)
    # Crear una imagen PIL a partir 
    # del array NumPy
    return Image.fromarray(
        matriz_np, 
        'RGB'
    )