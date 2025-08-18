

from PIL import Image

def create_rgb_image_pil(WIDTH, HEIGHT)\
        ->Image:
    """
    Crea una nueva imagen PIL 
    con fondo blanco y el tamaño 
    especificado.
    """
    # El modo "RGB" se utiliza para imágenes a color.
    modo = "RGB"
    tamaño = (WIDTH, HEIGHT)
    color_blanco = (255, 255, 255)  
    # (R, G, B) - 255 para cada canal 
    # representa el blanco.
    imagen = Image.new(
        modo, 
        tamaño, 
        color_blanco
    )
    return imagen

def create_rgba_image_pil(WIDTH, HEIGHT):
    """
    Crea una nueva imagen PIL con fondo 
    transparente y el tamaño especificado.
    Args:
        ancho: El ancho de la imagen en 
        píxeles.
        alto: El alto de la imagen en píxeles.
    Returns:
        Un objeto Image de PIL en modo 
        RGBA (Rojo, Verde, Azul, Alfa), 
        donde el alfa representa la 
        transparencia.
    """
    # El modo "RGBA" incluye un canal alfa para la transparencia.
    modo = "RGBA"
    tamaño = (WIDTH, HEIGHT)
    color_transparente = (0, 0, 0, 0)  # (R, G, B, A) - 0 para A significa completamente transparente.
    imagen = Image.new(modo, tamaño, color_transparente)
    return imagen