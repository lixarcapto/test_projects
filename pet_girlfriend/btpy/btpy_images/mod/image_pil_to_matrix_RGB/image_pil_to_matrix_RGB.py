

import tkinter as tk

from PIL import Image

def image_pil_to_matrix_RGB(imagen_pil: Image.Image) -> list[list[list[int]]] | None:
    """
    Convierte un objeto de imagen PIL a 
    una matriz RGB (lista de listas de 
    listas de enteros).
    """
    if not isinstance(imagen_pil, Image.Image):
        print("❌ Error: El objeto proporcionado no es una instancia válida de PIL.Image.Image.")
        return None

    # Asegurarse de que la imagen esté en modo RGB para obtener 3 canales.
    # Si la imagen es RGBA, convertirá a RGB descartando el canal alfa.
    # Si es escala de grises (L), la convertirá a RGB.
    if imagen_pil.mode not in ("RGB", "RGBA", "L"):
        print(f"Advertencia: La imagen está en modo '{imagen_pil.mode}'. "
              "Se intentará convertir a 'RGB' para obtener la matriz de 3 canales.")
        imagen_rgb = imagen_pil.convert("RGB")
    elif imagen_pil.mode == "RGBA":
        print("Advertencia: La imagen está en modo 'RGBA'. Se convertirá a 'RGB' y se ignorará el canal alfa.")
        imagen_rgb = imagen_pil.convert("RGB")
    else:
        imagen_rgb = imagen_pil.copy() # Hacemos una copia para no modificar el original

    ancho, alto = imagen_rgb.size
    matriz_rgb = []

    # getdata() devuelve una secuencia de píxeles.
    # Podemos iterar sobre ella y organizarla en filas.
    datos_pixel = list(imagen_rgb.getdata())

    for y in range(alto):
        fila = []
        for x in range(ancho):
            # Calcular el índice en la secuencia lineal de datos_pixel
            # (x, y) en una imagen 2D se mapea a un índice lineal: y * ancho + x
            pixel = datos_pixel[y * ancho + x]
            fila.append(list(pixel)) # Convertir la tupla de píxel a lista [R, G, B]
        matriz_rgb.append(fila)
    return matriz_rgb