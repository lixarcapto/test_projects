

from PIL import Image
import numpy as np

def matrix_rgb_to_image_pil(
        matriz_rgb: list[list[list[int]]]) -> Image.Image | None:
    """
    Convierte una matriz RGB de Python (lista de listas de listas de enteros) a un objeto PIL.Image.

    Args:
        matriz_rgb (list[list[list[int]]]): La matriz 3D que representa la imagen.
                                            Formato esperado: [[fila0_pixel0, fila0_pixel1, ...], ...],
                                            donde cada pixel es [R, G, B].
                                            Los valores R, G, B deben estar entre 0 y 255.

    Returns:
        Image.Image | None: Un objeto PIL.Image si la conversión es exitosa,
                            o None si la matriz no tiene el formato esperado o hay un error.
    """
    if not isinstance(matriz_rgb, list) or not matriz_rgb:
        print("❌ Error: La matriz RGB no es una lista válida o está vacía.")
        return None

    alto = len(matriz_rgb)
    ancho = len(matriz_rgb[0])

    # Validar que todas las filas tengan el mismo ancho y que los píxeles sean RGB
    for y, fila in enumerate(matriz_rgb):
        if not isinstance(fila, list) or len(fila) != ancho:
            print(f"❌ Error: La fila {y} no tiene el ancho esperado o no es una lista.")
            return None
        for x, pixel in enumerate(fila):
            if not isinstance(pixel, list) or len(pixel) != 3:
                print(f"❌ Error: El píxel en ({x}, {y}) no es una lista RGB de 3 elementos.")
                return None
            if not all(isinstance(c, int) and 0 <= c <= 255 for c in pixel):
                print(f"❌ Error: Los valores de color del píxel en ({x}, {y}) no son enteros entre 0 y 255.")
                return None

    try:
        # Convertir la lista de listas a un array NumPy
        # Esto es muy eficiente y es el formato preferido por Image.fromarray
        array_numpy = np.array(matriz_rgb, dtype=np.uint8)

        # Crear el objeto Image de PIL a partir del array NumPy
        # El modo 'RGB' es explícito para asegurar que se interprete correctamente
        imagen_pil = Image.fromarray(array_numpy, 'RGB')
        return imagen_pil

    except ValueError as e:
        print(f"❌ Error de valor al convertir la matriz a imagen PIL. Posiblemente formato incorrecto: {e}")
        return None
    except Exception as e:
        print(f"❌ Ocurrió un error inesperado al convertir la matriz RGB a imagen PIL: {e}")
        return None