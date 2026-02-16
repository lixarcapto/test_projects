


from tkinter import PhotoImage
from PIL import Image, ImageTk


def read_photoimage(route:str, size_x, 
        size_y)->PhotoImage:
    """
    Funcion que lee una imagen en la 
    direccion indicada y la carga como 
    un objeto PhotoImage de PIL
    """
    # Cargar la imagen con Pillow
    img = Image.open(route)

    # Reescalar la imagen (ejemplo usando Pillow)
    resized_img = img.resize((size_x, size_y))

    # Crear un objeto PhotoImage
    return ImageTk.PhotoImage(resized_img)    