

import math

def create_destiny_point(
        POINT,
        DISTANCE: float,
        DEGREES: float
        ) -> tuple[tuple[float, float], tuple[float, float]]:
    """
    Calcula un punto de destino trazando una línea desde un punto de origen
    con una distancia y un ángulo especificados.

    Args:
        origen_x (float): La coordenada X del punto de origen.
        origen_y (float): La coordenada Y del punto de origen.
        distancia (float): La longitud de la línea a trazar.
        grados_trazado (float): El ángulo en grados (0 a 360) desde el eje X positivo
                                (horizontal, hacia la derecha) en sentido antihorario.
                                (0 grados apunta a la derecha, 90 grados arriba, 180 izquierda, 270 abajo).

    Returns:
        tuple[tuple[float, float], tuple[float, float]]:
            Una tupla que contiene dos tuplas:
            1. El punto de origen: (origen_x, origen_y)
            2. El punto de destino: (destino_x, destino_y)
    """
    origen_x: float = POINT[0] 
    origen_y: float = POINT[1] 
    # Validaciones básicas de entrada
    if not all(isinstance(arg, (int, float)) for arg in [origen_x, origen_y, DISTANCE, DEGREES]):
        raise TypeError("Todas las entradas deben ser números (enteros o flotantes).")
    if DISTANCE < 0:
        raise ValueError("La distancia no puede ser negativa.")

    # Convertir grados a radianes, ya que las funciones trigonométricas de math
    # esperan ángulos en radianes.
    radianes = math.radians(DEGREES)

    # Calcular el desplazamiento en X (delta_x) y en Y (delta_y)
    # delta_x = distancia * cos(radianes)
    # delta_y = distancia * sin(radianes)
    # Nota: En sistemas de coordenadas gráficos (como imágenes), Y a menudo crece hacia abajo.
    # Si quieres que 0 grados sea a la derecha y 90 grados hacia ARRIBA (como en un plano cartesiano),
    # el seno se suma a Y. Si Y crece hacia abajo (como en la mayoría de las imágenes),
    # entonces para 90 grados (hacia arriba), Y debería disminuir, por lo que el seno se restaría de Y.
    # Aquí asumimos un plano cartesiano estándar donde Y positivo es hacia arriba.
    
    delta_x = DISTANCE * math.cos(radianes)
    delta_y = DISTANCE * math.sin(radianes)

    # Calcular el punto de destino
    destino_x = origen_x + delta_x
    destino_y = origen_y + delta_y

    punto_origen = (origen_x, origen_y)
    punto_destino = (destino_x, destino_y)

    return list(punto_destino)