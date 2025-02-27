


def is_function(ANY : any)->bool:
    """
    TESTED
    Función que verifica si 
    un dato enviado este tipo 
    función retornando verdadero 
    sí lo es y falso si no. Considera
    funciones a las funciones lambda,
    las funciones con nombre y los 
    metodos.
    """
    if(hasattr(ANY, "__name__")):
        return True
    return False