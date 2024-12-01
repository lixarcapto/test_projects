


def is_function(data)->bool:
    """
    Función que verifica si 
    un dato enviado este tipo 
    función retornando verdadero 
    sí lo es y falso si no
    """
    if(hasattr(data, "__name__")):
        return True
    return False