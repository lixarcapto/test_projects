

from ..dependences import Image, ImageTk

"""
    Funcion que lee una imagen en la direccion indicada
    y la carga como un objeto PhotoImage de PIL
"""
# return PhotoImage
def load_image_as_photoimage(ruta_imagen):
    """
    Función que carga una imagen como PhotoImage.
    Args:
      ruta_imagen: La ruta de la imagen a cargar.
    Returns:
      Un objeto PhotoImage de la imagen cargada o None si la imagen no se pudo cargar.
    """
    try:
      # Abrir la imagen como modo RGBA
      imagen = Image.open(ruta_imagen).convert('RGBA')
      # Redimensionar la imagen si se desea (opcional)
      # imagen = imagen.resize((ancho_nuevo, alto_nuevo))
      # Convertir la imagen a PhotoImage
      imagen_tk = ImageTk.PhotoImage(imagen)
      return imagen_tk
    except Exception as e:
      print(f"Error al cargar la imagen: {e}")
      return None
