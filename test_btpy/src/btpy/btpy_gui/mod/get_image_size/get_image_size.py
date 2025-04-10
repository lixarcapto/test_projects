
from PIL import Image, ImageTk  
# Importa las clases Image y ImageTk 
# de PIL

def get_image_size(PATH:str)->list[int]:
    """
    Function that obtains the size of 
    an image with the sent path, 
    returning a list of the size of a 
    rectangle; that is, an array with 
    the int width and height.
    """
    try:
        imagen_pil = Image.open(PATH)  
        # Abre la imagen con PIL
        width, height = imagen_pil.size 
        # Obtiene el ancho y la altura
        return [width, height]
    except Exception as e:
        print(f"Error al cargar la imagen: {e}")
        return None