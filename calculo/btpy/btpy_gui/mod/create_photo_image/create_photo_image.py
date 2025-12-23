


import tkinter as tk
from PIL import Image, ImageTk
from ....btpy_persistence.mod\
    .check_path.check_path import *

def create_photo_image(PATH:str, 
        SIZE_LIST:list[int] = [0, 0])\
        ->ImageTk.PhotoImage:
    """
    Funcion que crea un objeto Photoimage
    de Tkinter a partir de una PATH enviada.
    Tambien puede reajustar el tamaño si se 
    indican ambos lados. Es nesesario
    iniciar antes una ventana Tkinter para
    que funcione.
    """
    if(not check_path(PATH)):
        print("<!> Error in create_photo_image: The route sent is not valid.")
        return None
    imagen_pil = Image.open(PATH)
    if(SIZE_LIST != [0, 0]):
        imagen_pil = imagen_pil.resize((
            SIZE_LIST[0], 
            SIZE_LIST[1]
        ))
    return ImageTk.PhotoImage(imagen_pil)