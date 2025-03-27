


import tkinter as tk
from PIL import Image, ImageTk

def create_photo_image(PATH:str, 
        SIZE_LIST:list[int])\
        ->ImageTk.PhotoImage:
    """
    Funcion que crea un objeto Photoimage
    de Tkinter a partir de una PATH enviada.
    Tambien puede reajustar el tamaño si se 
    indican ambos lados. Es nesesario
    iniciar antes una ventana Tkinter para
    que funcione.
    """
    imagen_pil = Image.open(PATH)
    if(SIZE_LIST != [0, 0]):
        imagen_pil = imagen_pil.resize((
            SIZE_LIST[0], 
            SIZE_LIST[1]
        ))
    return ImageTk.PhotoImage(imagen_pil)