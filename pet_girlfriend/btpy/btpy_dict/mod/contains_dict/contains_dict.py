


def contains_dict(CONTAINER:dict[str, int],
        CONTENT:dict[str, int])->bool:
    """
    Funcion que verifica si un diccionario
    contiene las cantidades de otro 
    diccionario.
    """
    # Iteramos sobre las claves y valores del diccionario CONTENT.
    # Esto asegura que verificamos que CADA elemento de CONTENT
    # este presente y con la cantidad suficiente en CONTAINER.
    for key, content_value in CONTENT.items():
        # Paso 1: Verificar si la clave de CONTENT existe en CONTAINER.
        # Si una clave de CONTENT no esta en CONTAINER, entonces CONTAINER
        # no puede "contener" todo lo que CONTENT requiere.
        if key not in CONTAINER:
            return False

        # Paso 2: Si la clave existe, verificar si la cantidad en CONTAINER
        # es suficiente (mayor o igual) a la cantidad requerida en CONTENT.
        container_value = CONTAINER[key]
        if container_value < content_value:
            return False

    # Si el bucle termina sin retornar False, significa que todas las
    # claves de CONTENT estan en CONTAINER y con las cantidades suficientes.
    return True