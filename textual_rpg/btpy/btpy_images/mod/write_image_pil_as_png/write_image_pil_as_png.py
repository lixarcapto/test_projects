

from PIL import Image
import os # Import os for path manipulation and error checking

def write_image_pil_as_png(
        IMAGE_PIL: Image.Image, 
        PATH: str) -> bool:
    """
    Guarda un objeto de imagen PIL 
    (Pillow) como un archivo PNG.
    """
    # Validar que el objeto sea una instancia de Image.Image
    if not isinstance(IMAGE_PIL, Image.Image):
        print("❌ Error: El objeto proporcionado no es una instancia válida de PIL.Image.Image.")
        return False

    # Asegurarse de que la ruta de salida termine en .png (o añadirla si falta)
    if not PATH.lower().endswith(".png"):
        # Puedes optar por añadirlo o forzar un error, aquí lo añadimos para mayor flexibilidad
        print(f"Advertencia: La ruta de salida '{PATH}' no termina en '.png'. Se añadirá la extensión.")
        # Eliminar cualquier extensión existente antes de añadir .png
        nombre_base, _ = os.path.splitext(PATH)
        PATH = nombre_base + ".png"


    try:
        # El método .save() de un objeto Image es la forma estándar de guardar
        IMAGE_PIL.save(PATH, format="PNG")
        print(f"✅ Imagen guardada exitosamente en '{PATH}'")
        return True
    except IOError as e:
        print(f"❌ Error de E/S al guardar la imagen en '{PATH}': {e}")
        return False
    except ValueError as e:
        print(f"❌ Error de valor (ej. formato incorrecto) al guardar la imagen: {e}")
        return False
    except Exception as e:
        print(f"❌ Ocurrió un error inesperado al guardar la imagen: {e}")
        return False