



import tkinter as tk
from PIL import Image, ImageTk
import numpy as np

def matriz_rgb_to_photoimage(matriz_rgb):
    """
    Convierte una matriz RGB en un objeto PhotoImage de Tkinter.

    Args:
        matriz_rgb: Una matriz NumPy de forma (altura, anchura, 3) representando una imagen RGB.

    Returns:
        Un objeto PhotoImage de Tkinter.
    """

    # Convertir la matriz NumPy a 
    # una imagen PIL
    img = Image.fromarray(
        np.uint8(matriz_rgb))

    # Convertir la imagen PIL a PhotoImage
    photo = ImageTk.PhotoImage(img)

    return photo