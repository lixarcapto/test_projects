


def adjusts_to_threshold(
        NUMBER_TO_ADJUST: int | float,
        ADJUSTMENT: int | float,
        THRESHOLD: int | float
    ) -> int | float:
    """
    Ajusta un número sumando o restando 
    otro número, dependiendo de si el 
    primero es mayor o menor que
    un umbral, asegurando que el 
    resultado no supere
    el umbral.
    """
    result: int | float = 0
    if NUMBER_TO_ADJUST > THRESHOLD:
        result = NUMBER_TO_ADJUST - ADJUSTMENT
        if result < THRESHOLD:  # Verifica si el resultado es menor que el umbral
            result = THRESHOLD  # Si es así, lo establece al umbral
    elif NUMBER_TO_ADJUST < THRESHOLD:
        result = NUMBER_TO_ADJUST + ADJUSTMENT
        if result > THRESHOLD:  # Verifica si el resultado es mayor que el umbral
            result = THRESHOLD  # Si es así, lo establece al umbral
    else:
        result = NUMBER_TO_ADJUST
        # No se ajusta si es igual al umbral
    return result