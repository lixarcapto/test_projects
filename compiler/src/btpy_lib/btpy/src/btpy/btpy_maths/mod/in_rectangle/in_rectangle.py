


def in_rectangle(origen_point, ancho, alto):
    """
    Determina si un punto se encuentra 
    dentro de un rectángulo.
    """
    origen_x = origen_point[0]
    origen_y = origen_point[1]
    extension_point = get_extension_point()
    punto_x = extension_point[0]
    punto_y = extension_point[1]
    # Calculamos las coordenadas de 
    # la esquina inferior derecha del 
    # rectángulo
    x_max = origen_x + ancho
    y_max = origen_y + alto
    # Verificamos si las coordenadas 
    # del punto están dentro de los 
    # límites del rectángulo
    result = (origen_x <= punto_x <= x_max)\
        and (origen_y <= punto_y <= y_max)
    return result

def get_extension_point(origen_point, 
        ancho, alto):
    """
    Calcula el punto de extensión 
    derecho de un rectángulo.
    """
    # El punto de extensión derecho 
    # tiene la misma coordenada y que 
    # el punto de origen
    y = origen_point[1]
    # La coordenada x se calcula 
    # sumando el ancho al origen_x
    x = origen_point[0] + ancho
    return [x, y]