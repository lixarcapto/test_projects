


from PIL import Image

def create_png(matriz_rgb, nombre_archivo):
    """
    Guarda una matriz RGB como una imagen PNG.

    Args:
        matriz_rgb: Una lista de listas que representa una matriz RGB.
        nombre_archivo: El nombre del archivo PNG a guardar.
    """

    # Convertir la lista de listas a un array NumPy (opcional, pero mejora el rendimiento)
    import numpy as np
    matriz_np = np.array(matriz_rgb)

    # Crear una imagen PIL a partir del array NumPy
    imagen = Image.fromarray(matriz_np, 'RGB')

    # Guardar la imagen como PNG
    imagen.save(nombre_archivo, 'PNG')