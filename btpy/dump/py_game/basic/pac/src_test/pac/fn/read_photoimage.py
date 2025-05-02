


from PIL import Image
from tkinter import PhotoImage

"""
    Funcion que lee una imagen en la direccion indicada
    y la carga como un objeto PhotoImage de PIL
"""
# return PhotoImage
def read_photoimage(route:str):
        # Ajustar ancho y mantener relación de aspecto
        return PhotoImage(file = route)