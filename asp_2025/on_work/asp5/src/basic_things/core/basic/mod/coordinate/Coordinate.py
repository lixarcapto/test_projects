


class Coordinate:

    """
        Clase que representa coordenadas espaciales.
    """

    def __init__(self, x, y, z = 0):
        self._location_x = x
        self._location_y = y
        self._location_z = z

    """
        Funcion que realiza el movimiento indicado en el
        objeto dentro del escenario.
    """
    def move(self, direction_move, distance):
        x = self.get_x()
        y = self.get_y()
        if("n" == direction_move):
            y -= distance
        if("ne" == direction_move):
            y -= distance
            x -= distance
        if("nw" == direction_move):
            y -= distance
            x += distance
        elif("s" == direction_move):
            y += distance
        elif("se" == direction_move):
            y += distance
            x -= distance
        elif("sw" == direction_move):
            y += distance
            x += distance
        elif("e" == direction_move):
            x -= distance
        elif("w" == direction_move):
            x += distance
        self.set_x(x)
        self.set_y(y)

    # return int
    def get_x(self):
        return self._location_x

    def set_x(self, integer):
        self._location_x = integer

    # return int
    def get_y(self):
        return self._location_y

    def set_y(self, integer):
        self._location_y = integer

    # return int
    def get_z(self):
        return self._location_z

    def set_z(self, integer):
        self._location_z = integer
