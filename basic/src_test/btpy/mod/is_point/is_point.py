

def is_point(data, size:int):
        # valida el size
        if(not type(size) == int):
             raise Exception(
                "size parameter is not int"
             )
        if(not size == 2 
           or size == 3):
             raise Exception(
                f"size parameter cant be {size}"
             )
        # si no es lista
        if(not type(data) == list):
            return False
        # si es mas pequeño
        if(not len(data) == size):
            return False
        # si no son numeros
        for e in data: 
            if(not type(e) == int
            and not type(e) == float):
                return False
        return True