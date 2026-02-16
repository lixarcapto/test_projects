

def hex_to_RGB(HEX_COLOR:str)->list[int]:
    """
    Convierte un color en formato 
    hexadecimal (como #RRGGBB o #RRGGBBAA) 
    a una lista RGB.
    """
    if not isinstance(HEX_COLOR, str):
        raise ValueError("La entrada debe ser una cadena.")
    HEX_COLOR = HEX_COLOR.lstrip('#')  # Elimina el carácter '#' inicial si está presente
    if not (len(HEX_COLOR) == 6 or len(HEX_COLOR) == 8):
        raise ValueError("La cadena hexadecimal debe tener 6 u 8 caracteres (RRGGBB o RRGGBBAA).")

    try:
        # Convierte la cadena hexadecimal a entero
        entero_color = int(HEX_COLOR, 16)
    except ValueError:
        raise ValueError("Cadena hexadecimal inválida.")

    if len(HEX_COLOR) == 6:
        # Extrae los componentes R, G y B
        r = (entero_color >> 16) & 0xFF
        g = (entero_color >> 8) & 0xFF
        b = entero_color & 0xFF
        return [r, g, b]
    elif len(HEX_COLOR) == 8:
        # Extrae los componentes R, G, B y A
        r = (entero_color >> 24) & 0xFF
        g = (entero_color >> 16) & 0xFF
        b = (entero_color >> 8) & 0xFF
        a = entero_color & 0xFF
        return [r, g, b, a]