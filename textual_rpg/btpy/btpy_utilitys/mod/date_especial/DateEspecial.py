


from .NAMES_DATE import*
from .calcule_first_day import*
from ....btpy_data_types.mod.switch.Switch import Switch

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
    * añadir las diferencias de estaciones 
        en el calendario juliano y gregoriano
    * añadir cambio de estacion para hemisferio
    norte y sur
    """
    SEASON_CHANGE_DAYS_NORTH = {
        "summer":{"day_number":21,"month":6},
        "spring":{"day_number":21,"month":3},
        "automn":{"day_number":23,"month":9},
        "winter":{"day_number":21,"month":12}
    }
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
    class CALENDAR:
        JULIAN = "julian"
        GREGORIAN = "gregorian"

    def __init__(self) -> None:
        self.__day = 0
        self.__day_number = 0
        self.__week = 0
        self.__month = 0
        self.year_to_leap = 0
        self.__year = 0
        self.__season = ""
        self.calendar = "gregorian"
        self.hemisphere = "north"
        self.is_leap_year = Switch()

    def set_leap_year(self, BOOL):
        self.is_leap_year = Switch(BOOL)

    def set_english_date(self, 
            DATE_STRING:str):
        date_dict = self.get_date_dict(
            DATE_STRING)
        days_remaining = self\
            .get_remaining_days(
                date_dict["day"],
                date_dict["month"])
        # ajusta si es año biciesto
        is_leap_year = self.set_leap_year(
            date_dict["year"])
        self.set_leap_year(is_leap_year)
        # determina el dia de inicio
        dict_result = calcule_first_day(
            date_dict["year"])
        # ajusta el dia y el año
        self.__day = dict_result["index_day"]
        self.calendar = dict_result["calendar"]
        self.__year = date_dict["year"]
        # avansa hasta llegar al dia indicado
        for i in range(days_remaining -1):
            self.advance_one_day()

    def get_date_dict(self, DATE_STRING):
        # divide la fecha
        date_arr = DATE_STRING.split("/")
        # traduce los datos a int
        year = int(date_arr[0])
        month = int(date_arr[1])
        days_number = int(date_arr[2])
        return {
            "year" : year,
            "month" : month,
            "day": days_number
        }

    def get_remaining_days(self, 
            DAY_NUMBER, MONTH_NUMBER):
        """
        Calcula el numero de dias 
        restantes
        """
        i = 0
        days_remaning = DAY_NUMBER
        for day_number in self.MONTH_DAYS:
            if(i == MONTH_NUMBER -1): break
            days_remaning += day_number
            i += 1
        return days_remaning

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
        + self.__season.capitalize()\
        + f" {self.__year} " \
        + f"of the {self.calendar.capitalize()} calendar "\
        + f"in {self.hemisphere} hemisphere."
    
    def get_season(self):
        season_key = self.get_season_key(
            self.__day_number,
            self.__month,
            self.is_leap_year
        )
        self.is_leap_year = Switch(
            self.is_leap_year)
        self.__season = season_key

    def get_season_key(self, DAY_NUMBER,
            MONTH_INDEX, IS_LEAP_YEAR):
        season_result = ""
        collection = self.SEASON_CHANGE_DAYS_NORTH
        for season_key in self.SEASON_CHANGE_DAYS_NORTH:
            dict_season = collection[season_key]
            if(dict_season["day_number"] == DAY_NUMBER
            and dict_season["month"] == MONTH_INDEX):
                season_result = season_key
        return season_key

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
            self.get_season()
        if(self.__day_number >= self\
            .get_days_by_month(self.__month)):            
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
        

    