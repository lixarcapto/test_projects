

import random

def choose_probability(
            PROBABILITY_LIST: list) -> str:
    """
    Elige una clave de una lista de pares [clave, valor] aleatoriamente,
    basado en los porcentajes de probabilidad proporcionados en los valores.

    Args:
        lista_probabilidades: Una lista de pares [clave, valor], donde:
            - clave (str): Es la clave a elegir.
            - valor (number): Es la probabilidad de elegir la clave (0-100).
            Las probabilidades deben sumar 100.

    Returns:
        La clave elegida aleatoriamente.

    Raises:
        ValueError: Si las probabilidades no suman 100 o si algún porcentaje está fuera del rango 0-100.
    """
    total_probabilidad = 0
    for _, probabilidad in PROBABILITY_LIST:
        if not 0 <= probabilidad <= 100:
            raise ValueError("Los porcentajes deben estar entre 0 y 100.")
        total_probabilidad += probabilidad

    if not abs(total_probabilidad - 100) < 1e-6:  # Usamos una tolerancia para la comparación de punto flotante
        raise ValueError(f"Las probabilidades deben sumar 100. Suma actual: {total_probabilidad}")

    # Creamos una lista de puntos de corte acumulativos
    puntos_de_corte = []
    probabilidad_acumulada = 0
    for clave, probabilidad in PROBABILITY_LIST:
        probabilidad_acumulada += probabilidad
        puntos_de_corte.append((clave, probabilidad_acumulada))

    # Generamos un número aleatorio entre 0 y 100
    numero_aleatorio = random.uniform(0, 100)

    # Encontramos el intervalo en el que cae el número aleatorio
    for clave, punto_de_corte in puntos_de_corte:
        if numero_aleatorio <= punto_de_corte:
            return clave

    # Esto no debería alcanzarse, pero se incluye para asegurar que siempre se retorne algo.
    return PROBABILITY_LIST[-1][0]