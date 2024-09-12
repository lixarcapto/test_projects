


class RangeSpace:

    """
    Clase para almacenar representaciones 
    de espacios utilizando intervalos de 
    ejes límites.
    """
    def __init__(self) -> None:
        self.range_x = [0, 0]
        self.range_y = [0, 0]
        self.range_z = [0, 0]

    def write(self):
        txt = f"x:{self.range_x}, "
        txt += f"y:{self.range_y}, "
        txt += f"z:{self.range_z}"
        return txt
    
    def __str__(self):
        return self.write()