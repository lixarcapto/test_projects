


from PIL import Image, ImageEnhance

def clarify_image_pil(IMAGE_PIL:Image, 
        FACTOR:float)->Image:
    """
    Aclara una imagen PIL.

    Args:
        imagen: El objeto Image de PIL 
        que se va a aclarar.
        factor: Un valor flotante que 
        controla el brillo.
            1.0 devuelve la imagen 
            original, valores mayores 
            la aclaran.
    Returns:
        Un nuevo objeto Image de PIL que representa la imagen aclarada.
    """
    enhancer = ImageEnhance.Brightness(
        IMAGE_PIL)
    imagen_aclarada = enhancer.enhance(
        FACTOR)
    return imagen_aclarada