

from PIL import Image
import io # Módulo para trabajar con flujos de E/S en memoria

def binary_to_image_pil(
        contenido_binario: bytes)\
        -> Image.Image | None:
    """
    Convierte una secuencia de bytes 
    binarios a un objeto de imagen PIL.
    """
    if not isinstance(contenido_binario, bytes):
        print("❌ Error: El contenido proporcionado no es una secuencia de bytes.")
        return None
    try:
        # Usamos BytesIO para leer los bytes como si fueran un archivo
        buffer_bytes = io.BytesIO(contenido_binario)
        # Cargamos la imagen desde el búfer
        imagen_pil = Image.open(buffer_bytes)
        print("✅ Contenido binario convertido a objeto PIL.Image exitosamente.")
        return imagen_pil
    except Exception as e:
        print(f"❌ Error al convertir binario a objeto PIL.Image: {e}")
        return None