


from ..citizen.citizen_constants import*

class Passport:

    """
    Esta clase permite almacenar una 
    pequeña cantidad de datos relacionados
    a un personaje como recuerdos de otros
    personajes.
    """

    def __init__(self):
        self.full_name:str = ""
        self.profession:int = 0
        self.culture:int = 0
        self.id_number:int = 0

    def write(self)->str:
        txt = self.full_name + " "
        txt += f", an {self.culture} "
        txt += self.profession
        return txt
