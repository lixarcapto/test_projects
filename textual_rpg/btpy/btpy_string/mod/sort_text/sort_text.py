

def sort_text(text, limit_char_in_line):
    """
    Función que ajusta el texto 
    para cortar correctamente
    las palabras al llegar al límite 
    de caracteres por línea.
    """
    result = ""
    line_length = 0
    should_insert_newline = False
    for char in text:
        result += char
        line_length += 1
        if line_length >= limit_char_in_line:
            should_insert_newline = True
        if should_insert_newline and char in " .,;:":
            result = result.rstrip()  
            # Elimina espacios antes 
            # de insertar el salto de línea
            result += "\n"
            line_length = 0  
            # Reinicia el contador de 
            # caracteres en la nueva línea
            should_insert_newline = False
    return result
