


def percent_to_index(percent, limit):
    """
    convierte un porcentaje a un 
    índice dentro de un rango 
    específico.
    """
    part = 100 / limit
    percent_for_index = 0
    for index in range(limit):
        percent_for_index = index * part
        if(percent <= percent_for_index):
            return index
    return limit