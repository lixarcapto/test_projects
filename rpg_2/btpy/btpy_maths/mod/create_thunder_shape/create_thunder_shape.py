


import random
import math

def create_thunder_shape(
    x_origen: int,
    y_origen: int,
    longitud_max_segmento: int,
    num_segmentos: int,
    desviacion_max_grados: float,
    direccion_base_grados: float = 270.0 # Por defecto, apunta hacia abajo
) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    """
    Genera una lista de segmentos de línea (pares de puntos) que simulan un relámpago aleatorio.

    Args:
        x_origen (int): Coordenada X del punto inicial del relámpago.
        y_origen (int): Coordenada Y del punto inicial del relámpago.
        longitud_max_segmento (int): La longitud máxima de cada segmento individual del relámpago.
                                     Los segmentos serán de 1 a esta longitud.
        num_segmentos (int): La cantidad total de segmentos que formarán el relámpago.
        desviacion_max_grados (float): El ángulo máximo en grados en que cada segmento puede desviarse
                                       de la dirección anterior (o la dirección base).
                                       Un valor más alto crea un relámpago más "zigzagueante".
        direccion_base_grados (float): La dirección inicial general del relámpago en grados.
                                       0° = derecha, 90° = arriba, 180° = izquierda, 270° = abajo.
                                       (Asumiendo Y crece hacia abajo, como en gráficos).

    Returns:
        list[tuple[tuple[int, int], tuple[int, int]]]: Una lista de tuplas,
            donde cada tupla interna representa un segmento de línea ((x1, y1), (x2, y2)).
    """
    if not all(isinstance(arg, (int, float)) for arg in [x_origen, y_origen, longitud_max_segmento, num_segmentos, desviacion_max_grados, direccion_base_grados]):
        raise TypeError("Todos los argumentos deben ser números.")
    if longitud_max_segmento <= 0 or num_segmentos <= 0:
        raise ValueError("Longitud_max_segmento y num_segmentos deben ser mayores que 0.")
    if desviacion_max_grados < 0:
        raise ValueError("Desviacion_max_grados no puede ser negativa.")

    segmentos_relampago = []
    
    # El punto actual comienza en el origen
    current_x, current_y = x_origen, y_origen
    
    # La dirección actual comienza como la dirección base
    current_direccion = direccion_base_grados

    for _ in range(num_segmentos):
        # Generar una pequeña desviación aleatoria del ángulo
        desviacion_angular = random.uniform(-desviacion_max_grados, desviacion_max_grados)
        current_direccion += desviacion_angular

        # Asegurarse de que la dirección se mantenga entre 0 y 360 grados
        current_direccion = current_direccion % 360.0
        if current_direccion < 0:
            current_direccion += 360.0

        # Generar una longitud aleatoria para el segmento
        longitud_segmento = random.randint(1, longitud_max_segmento)

        # Convertir dirección a radianes (Pillow y la mayoría de sistemas gráficos
        # tienen el eje Y positivo hacia abajo, por lo que ajustamos el seno para esto).
        # Para que 90 grados sea "arriba" en una imagen (Y disminuye), y 270 "abajo" (Y aumenta).
        radianes = math.radians(current_direccion)
        
        # Calcular delta_x y delta_y para el nuevo punto
        # Para X: cos(angle)
        # Para Y: sin(angle) para un plano cartesiano estándar (Y hacia arriba)
        #         -sin(angle) o invertir el ángulo para un plano gráfico (Y hacia abajo)
        # La forma más fácil con PIL es usar la convención matemática y luego ajustar Y.
        # O, si definimos 0 grados como derecha y 270 como abajo (que es el default),
        # entonces cos(angle) para X y sin(angle) para Y funcionan si Y crece hacia abajo.
        
        # Asumiendo que Y positivo es ABAJO (como en la mayoría de los sistemas de coordenadas de imágenes)
        delta_x = longitud_segmento * math.cos(radianes)
        delta_y = longitud_segmento * math.sin(radianes) # Si 270 es abajo, sin(270) es -1, por lo que Y baja.

        # Calcular el punto final del segmento
        next_x = current_x + delta_x
        next_y = current_y + delta_y

        # Añadir el segmento a la lista (convertir a enteros para píxeles)
        segmentos_relampago.append(((int(current_x), int(current_y)), (int(next_x), int(next_y))))

        # El punto final de este segmento se convierte en el origen del siguiente
        current_x, current_y = next_x, next_y

    return segmentos_relampago