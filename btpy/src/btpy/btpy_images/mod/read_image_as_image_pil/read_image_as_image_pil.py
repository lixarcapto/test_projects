

from PIL import Image
import os

def read_image_as_image_pil(
        PATH: str)\
        -> Image.Image | None:
    """
    Lee un archivo de imagen y lo convierte a un objeto PIL.Image en modo RGBA.
    Esto preserva la transparencia de archivos PNG.
    """
    if not os.path.exists(PATH):
        print(f"❌ Error: El archivo de imagen no se encontró en la ruta: '{PATH}'")
        return None
    
    try:
        # 1. Abrir la imagen en su modo original.
        imagen_pil = Image.open(PATH)
        
        # 2. Convertir la imagen directamente a RGBA.
        # Esto conservará la transparencia si la imagen original (ej. PNG) la tenía.
        # Si la imagen original no tenía alfa (ej. JPG), se añadirá un canal alfa completamente opaco.
        imagen_pil = imagen_pil.convert("RGBA")
        
        print(f"✅ Imagen '{PATH}' leída exitosamente como objeto PIL.Image en modo RGBA.")
        return imagen_pil
    
    except Image.UnidentifiedImageError:
        print(f"❌ Error: No se pudo identificar el formato de la imagen en '{PATH}'.")
        return None
    except FileNotFoundError:
        print(f"❌ Error: El archivo '{PATH}' no se encontró.")
        return None
    except Exception as e:
        print(f"❌ Ocurrió un error inesperado al leer la imagen '{PATH}': {e}")
        return None