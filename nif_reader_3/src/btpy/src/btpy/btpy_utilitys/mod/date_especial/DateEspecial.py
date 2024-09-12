


from .NAMES_DATE import*
from .calcule_first_day import*
from ....btpy_utilitys.mod.switch.Switch import Switch

class DateEspecial:

    """
    TODO:
    * añadir que las estaciones cambian en 
    determinado dia del mes.
    * añadir los años tropicales
    * añadir un sistema automatico de fechas
    de referencia para los dias de la semana
    * añadir el numero de semana del mes
    * mejorar el encapsulamiento
    * añadir soporte en español
    * añadir soporte para fechas latinas
    * añadir un sistema de siglos romanos
    """

    SEASONS_BY_MONTH = [
        {"north":"winter", "south":"summer"},# enero
        {"north":"winter", "south":"summer"},# febrero
        {"north":"spring", "south":"autumn"},# marzo
        {"north":"spring", "south":"autumn"},# abril
        {"north":"spring", "south":"autumn"},# mayo
        {"north":"summer", "south":"winter"},# junio
        {"north":"summer", "south":"winter"},# julio
        {"north":"summer", "south":"winter"},# agosto
        {"north":"autumn", "south":"spring"},# septiembre
        {"north":"autumn", "south":"spring"},# octubre
        {"north":"autumn", "south":"spring"},# noviembre
        {"north":"winter", "south":"summer"}# diciembre
    ]
    MONTH_DAYS = [
        31,
        28,
        31,
        30,
        31,
        30,
        31,
        31,
        30,
        31,
        30,
        31
    ]
    DAYS_BY_WEEK = 7
    WEEKS_BY_MONTH = 4
    MONTHS_BY_YEAR = 12
    LEAP_YEAR_INTERVAL = 4
    class HEMISPHERE:
        NORTH = "north"
        SOUTH = "south"

    def __init__(self) -> None:
        self.__day = 0
        self.__day_number = 0
        self.__week = 0
        self.__month = 0
        self.year_to_leap = 0
        self.__year = 0
        self.__season = ""
        self.hemisphere = "north"
        self.is_leap_year = Switch()

    def set_leap_year(self, BOOL):
        self.is_leap_year = Switch(BOOL)

    def set_english_date(self, DATE_STRING):
        date_arr = DATE_STRING.split("/")
        year = int(date_arr[0])
        month = int(date_arr[1])
        days_number = int(date_arr[2])
        i = 0
        days_remaning = days_number
        for day_number in self.MONTH_DAYS:
            if(i == month -1): break
            days_remaning += day_number
            i += 1
        is_leap_year = self.set_leap_year(
            year)
        self.set_leap_year(is_leap_year)
        self.__day = calcule_first_day(year)
        self.__year = year
        for i in range(days_remaning -1):
            self.advance_one_day()

    def write_date(self):
        return ""\
        + f"{self.__year +1}/" \
        + f"{self.__month +1 }/" \
        + f"{self.__day_number +1}"
    
    def write_narrative(self):
        return ""\
        + f"{DAY_NAMES[self.__day]}, " \
        + f"the {self.__day_number +1}th of " \
        + f"{MONTH_NAMES[self.__month]}, " \
        + self.get_season(self.__month).capitalize()\
        + f" {self.__year}."
    
    def get_season(self, MONTH_INDEX, 
            /,IS_LEAP_YEAR = False):
        dict = self.SEASONS_BY_MONTH[MONTH_INDEX]
        self.is_leap_year = Switch(
            IS_LEAP_YEAR)
        return dict[self.hemisphere]

    def get_days_by_month(self, MONTH_INDEX):
        if(MONTH_INDEX == 1):
            if self.is_leap_year.is_true(): 
                return 29
                print("self.is_leap_year")
            else: 
                return 28
        return self.MONTH_DAYS[MONTH_INDEX]

    def advance_one_day(self):
        self.__day += 1
        self.__day_number += 1
        if(self.__day >= self.DAYS_BY_WEEK):
            self.__day = 0
        if(self.__day_number >= self\
            .get_days_by_month(self.__month)):
            self.__season = self.get_season(
                self.__month
            )
            self.__month += 1
            self.__day_number = 0
        if(self.__month >= self.MONTHS_BY_YEAR):
            self.__month = 0
            self.__year += 1
            if(self.year_to_leap == self.LEAP_YEAR_INTERVAL):
                self.year_to_leap = 0
                print("leap_year")
                self.is_leap_year.switch()
            else:
                self.year_to_leap += 1
                self.is_leap_year.switch()

    def is_leap_year(YEAR:int)->bool:
        """
        Determina si un año es bisiesto.
        True si el año es bisiesto, False en 
        caso contrario.
        """
        if YEAR % 4 == 0:
            if YEAR % 100 == 0:
                return YEAR % 400 == 0
            else:
                return True
        else:
            return False
        

    