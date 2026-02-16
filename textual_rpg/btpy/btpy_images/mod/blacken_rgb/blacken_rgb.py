

def blacken_rgb(RGB_LIST:list[int], 
        FACTOR:float = 0.1)->list[int]:
    """
    Oscurece un color RGB.
    Args:
        color_rgb: Una tupla o lista 
        de 3 elementos que representa 
        un color RGB (R, G, B), donde 
        los valores están en el rango 
        de 0 a 255.
        factor: Un valor flotante entre 
        0 y 1 que determina cuánto se 
        va a oscurecer el color.
        0 no cambia el color, 1 lo 
        oscurece completamente a negro. 
        El valor por defecto es 0.1.
    Returns:
        Una tupla de 3 elementos que 
        representa el color RGB oscurecido.
    """
    r, g, b = RGB_LIST
    # Asegura que el factor esté en el 
    # rango de 0 a 1
    FACTOR = max(0, min(1, FACTOR))
    # Calcula los nuevos valores de color
    nuevo_r = int(r * (1 - FACTOR))
    nuevo_g = int(g * (1 - FACTOR))
    nuevo_b = int(b * (1 - FACTOR))
    return [nuevo_r, nuevo_g, nuevo_b]