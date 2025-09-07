


from .time_const import*

class TimeSp:

    """
    Clase que sirve para manejar el 
    sistema de tiempos del simulador.
    """

    DAYS_AT_MONTH = 4
    MONTHS_AT_YEAR = 4
    

    def __init__(self):
        self.day:int = 0
        self.day_number:int = 0
        self.month:int = 0
        self.year:int = 0

    def write_age(self)->str:
        """
        Escribe la edad de un personaje.
        """
        return f"{self.year} years old"
    
    def get_day(self)->str:
        return KEY_DAY_TUPLE[self.day]
    
    def get_month(self)->str:
        return KEY_MONTH_TUPLE[self.month]

    def write_date(self)->str:
        """
        Escribe la fecha actual.
        """
        txt = ""\
        + f"{self.get_day()} " \
        + f"{self.day_number} from "\
        + f"{self.get_month()} "\
        + f"in the year {self.year}"
        return txt

    def advance_one_day(self):
        self.day += 1
        self.day_number += 1
        if(self.DAYS_AT_MONTH == self.day):
            self.day = 0
            self.month += 1
        if(self.MONTHS_AT_YEAR == self.month):
            self.month = 0
            self.year += 1
            self.day_number = 0
        