



from PIL import Image

def image_size(image_route:str)->dict:
    # Abrir la imagen
    imagen = Image.open(image_route)
    # Obtener el ancho y alto
    ancho, alto = imagen.size
    return {"x":ancho, "y":alto}
