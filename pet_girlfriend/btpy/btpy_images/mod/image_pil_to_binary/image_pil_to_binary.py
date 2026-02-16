


from PIL import Image
import io # Módulo para trabajar con flujos de E/S en memoria

def image_pil_to_binary(
        imagen_pil: Image.Image, 
        formato: str = "PNG")\
        -> bytes | None:
    """
    Convierte un objeto de imagen PIL 
    (Pillow) a una secuencia de bytes 
    binarios.
    imagen_pil (Image.Image): El objeto 
    de imagen de Pillow.
    formato (str): 
        * "PNG" 
        * "JPEG"
        * "BMP"
    Debe ser un formato soportado 
    por Pillow. Por defecto es "PNG".
    """
    if not isinstance(imagen_pil, Image.Image):
        print("❌ Error: El objeto proporcionado no es una instancia de PIL.Image.Image.")
        return None

    # Aseguramos que el formato sea 
    # mayúsculas para compatibilidad 
    # con Pillow
    formato = formato.upper()

    try:
        # Creamos un búfer de bytes en memoria
        buffer_bytes = io.BytesIO()
        
        # Guardamos la imagen PIL en este búfer en el formato especificado
        imagen_pil.save(buffer_bytes, format=formato)
        
        # Obtenemos la secuencia de bytes del búfer
        contenido_binario = buffer_bytes.getvalue()
        
        print(f"✅ Objeto PIL convertido a binario en formato '{formato}' exitosamente.")
        return contenido_binario
        
    except ValueError as e:
        print(f"❌ Error al convertir la imagen: Formato '{formato}' no soportado o inválido. Detalles: {e}")
        return None
    except Exception as e:
        print(f"❌ Ocurrió un error inesperado al convertir la imagen PIL a binario: {e}")
        return None