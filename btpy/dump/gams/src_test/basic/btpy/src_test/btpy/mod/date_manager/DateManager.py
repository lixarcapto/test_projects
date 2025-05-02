


from .svc.move_forward_one_day import*
from .DateManagerData import DateManagerData
from .svc.write_date import write_date

class DateManager:

    """
        Clase facada de tipo toolkit; es decir no es una
        entidad y debe manejarse mediante funciones.
    """

    def __init__(self):
        self.data = DateManagerData()

    def create_date_manager_data(self):
        return DateManagerData()

    def move_forward_one_day(self):
        self.data = move_forward_one_day(self.data)

    def write_date(self, lenguage = "english"):
        return write_date(self.data, lenguage)
