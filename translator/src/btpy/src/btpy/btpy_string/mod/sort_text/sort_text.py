


def sort_text( TEXT, LIMIT_CHAR_IN_LINE):
        """
        Funcion que ordena el texto para 
        cortar correctamente las palabras 
        finales
        """
        result = ""
        counter = 0
        prepair_jump = False
        for char in TEXT:
            result += char
            counter += 1
            if counter % LIMIT_CHAR_IN_LINE == 0:
                prepair_jump = True
            if(prepair_jump):
                if(char in " .,;:"):
                    prepair_jump = False 
                    result += "\n"
        return result
