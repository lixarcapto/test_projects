

def is_point_2d(data)->bool:
     """
      Función que verifica  el dato 
      enviado es un punto 2D
     """
     return __is_point(data, 2)


def is_point_3d(data)->bool:
     """
      Función que verifica  el dato 
      enviado es un punto 3D
     """
     return __is_point(data, 3)

def __is_point(data, size:int):
        # valida el size
        if(not type(size) == int):
             return False
        if((not size == 2)
           or (size == 3)):
             return False
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