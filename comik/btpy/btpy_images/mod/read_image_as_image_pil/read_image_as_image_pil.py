

from PIL import Image
import os # Import os for path checking

def read_image_as_image_pil(
        PATH: str)\
        -> Image.Image | None:
    """
    Lee un archivo de imagen (
    JPG, PNG, BMP, etc.) y lo 
    convierte en un objeto PIL.Image.
    """
    # 1. Verificar si el archivo existe
    if not os.path.exists(PATH):
        print(f"❌ Error: El archivo de imagen no se encontró en la ruta: '{PATH}'")
        return None
    
    try:
        # 2. Abrir la imagen usando Image.open()
        # El método open() detecta automáticamente el formato de la imagen.
        # .convert("RGB") es opcional pero recomendable para asegurar un formato de color consistente,
        # especialmente si vas a manipular la imagen más tarde. Si no lo usas, la imagen
        # mantendrá su modo original (ej. RGBA para PNGs con transparencia, L para escala de grises).
        imagen_pil = Image.open(PATH).convert("RGB")
        
        print(f"✅ Imagen '{PATH}' leída exitosamente como objeto PIL.Image.")
        return imagen_pil
    
    except Image.UnidentifiedImageError:
        print(f"❌ Error: No se pudo identificar el formato de la imagen en '{PATH}'. "
              "Asegúrate de que sea un archivo de imagen válido y soportado por Pillow.")
        return None
    except FileNotFoundError: # Aunque ya lo chequeamos, es buena práctica mantenerlo para otros casos.
        print(f"❌ Error: El archivo '{PATH}' no se encontró.")
        return None
    except Exception as e:
        print(f"❌ Ocurrió un error inesperado al leer la imagen '{PATH}': {e}")
        return None