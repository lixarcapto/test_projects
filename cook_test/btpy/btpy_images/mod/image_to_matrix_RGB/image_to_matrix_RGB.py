

import tkinter as tk
from PIL import Image, ImageTk
import numpy as np

def image_to_matrix_RGB(image_pil:Image)\
        ->list[list]:
    # Convertir la matriz NumPy a 
    # una imagen PIL
    return Image.fromarray(
        np.uint8(image_pil))