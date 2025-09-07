


def find_point_in_grid(
    POINT:list[int],
    grid_ancho: int,
    grid_alto: int,
    ancho_rectangulo: int,
    alto_rectangulo: int
) -> tuple[int, int] | None:
    """
    Determina la coordenada (fila, columna) del rectángulo dentro de una cuadrícula
    en el que se encuentra un punto dado.

    Args:
        punto_x: La coordenada x del punto.
        punto_y: La coordenada y del punto.
        grid_ancho: El número de columnas en la cuadrícula.
        grid_alto: El número de filas en la cuadrícula.
        ancho_rectangulo: El ancho de cada rectángulo en la cuadrícula.
        alto_rectangulo: El alto de cada rectángulo en la cuadrícula.

    Returns:
        Una tupla (fila, columna) que representa la coordenada del rectángulo,
        o None si el punto está fuera de la cuadrícula.

    Raises:
        TypeError: Si alguno de los argumentos no es de tipo numérico (int o float).
        ValueError: Si alguno de los argumentos de dimensión (ancho_rectangulo,
                    alto_rectangulo, grid_ancho, grid_alto) es menor o igual a cero.
    """
    punto_x: float = POINT[0]
    punto_y: float = POINT[1]
    # Validación de tipo de argumentos
    if not all(
        isinstance(arg, (int, float))
        for arg in [
            punto_x,
            punto_y,
            grid_ancho,
            grid_alto,
            ancho_rectangulo,
            alto_rectangulo,
        ]
    ):
        raise TypeError("Todos los argumentos deben ser numéricos (int o float)")

    # Validación de valores de argumentos
    if ancho_rectangulo <= 0 or alto_rectangulo <= 0 or grid_ancho <= 0 or grid_alto <= 0:
        raise ValueError(
            "Las dimensiones de los rectángulos y la cuadrícula deben ser mayores que cero"
        )

    # Si el punto está fuera de los límites de la cuadrícula, retorna None
    if punto_x < 0 or punto_x >= grid_ancho * ancho_rectangulo or punto_y < 0 or punto_y >= grid_alto * alto_rectangulo:
        return None

    # Calcula la columna y la fila del rectángulo
    columna = int(punto_x // ancho_rectangulo)
    fila = int(punto_y // alto_rectangulo)

    return fila, columna