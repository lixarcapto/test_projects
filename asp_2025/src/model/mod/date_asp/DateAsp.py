

from btpy.Btpy import Btpy

class DateAsp:

    """
    Esta clase sirve como un calendario
    para las fechas y sistemas de tiempo
    del simulador; no se corresponde con
    las del mundo real.
    """

    DAY_NAMES_TUPLE:tuple[str] = (
        "LIGHT_DAY",
        "TWILIGHT_DAY",
        "SHADOWS_DAY"
    )

    MONTH_NAMES_TUPLE:tuple[str] = (
        "summer", 
        "winter", 
        "autumn", 
        "spring"
    )

    YEARS_CYCLE_NAMES_TUPLE:tuple[str] = (
        "FROG",   # 0
        "RABBIT", # 1
        "DOG",    # 2
        "CAT",    # 3
        "DRAGON", # 4
        "SNAKE",  # 5
        "RAVEN",  # 6
        "PENGUIN" # 7
    )

    DAYS_BY_MONTH:int = 3
    MONTHS_BY_YEAR:int = 4
    MAX_YEARS:int = 10000
    DAYS_BY_YEAR:int = MONTHS_BY_YEAR \
        * DAYS_BY_MONTH
    
    def __init__(self):
        self.__day_code:int = 0
        self.__day:int = 0
        self.__month:int = 0
        self.__year:int = 0
        self.__cycle_year:int = 0

    def reset(self):
        """
        Resetea todos los contadores.
        """
        self.__day_code = 0
        self.__day = 0
        self.__month = 0
        self.__year = 0
        self.__cycle_year = 0

    def get_days_by_month(self)->int:
        """
        Retorna la cantidad maxima de 
        dias por cada mes.
        """
        return DateAsp.DAYS_BY_YEAR
    
    def get_days_by_year(self)->int:
        """
        Retorna la cantidad maxima de 
        dias por cada año.
        """
        return DateAsp.DAYS_BY_YEAR
    
    def get_months_by_year(self)->int:
        """
        Retorna la cantidad maxima de 
        meses por cada año.
        """
        return DateAsp.MONTHS_BY_YEAR
    
    def get_years_by_cycle_year(self)->int:
        """
        Retorna la cantidad maxima de 
        años por cada ciclo de años.
        """
        return len(DateAsp\
            .YEARS_CYCLE_NAMES_TUPLE)

    def __str__(self):
        return self.write_date()

    def write_date(self)->str:
        return ""\
            + f"{self.__day_code} " \
            + f"{self.get_day_name()}({self.__day}) " \
            + f"{self.get_month_name()} " \
            + f"{self.__year} "
    
    def set_year(self, YEAR:int):
        in_range = Btpy.in_range(
            YEAR, 
            [0, DateAsp.MAX_YEARS]
        )
        if(not in_range):
            raise Exception("the parameter AGE that is outside the limit range")
        self.__year = YEAR
    
    def set_day(self, DAY:int):
        in_range = Btpy.in_range(
            DAY, 
            [0, DateAsp.DAYS_BY_MONTH]
        )
        if(not in_range):
            raise Exception("the parameter DAY that is outside the limit range")
        self.__day = DAY

    def set_month(self, MONTH:int):
        in_range = Btpy.in_range(
            MONTH, 
            [0, DateAsp.MONTHS_BY_YEAR]
        )
        if(not in_range):
            raise Exception("the parameter MONTH that is outside the limit range")
        self.__month = MONTH

    def get_year(self):
        return self.__year
    
    def get_day_code(self)->int:
        """
        Retorna el codigo numerico
        del dia actual; este identifica
        al dia dentro del año.
        """
        return self.__day_code
    
    def get_day(self)->int:
        """
        Retorna el numero del dia actual.
        """
        return self.__day

    def get_month(self)->int:
        """
        Retorna el numero del mes actual.
        """
        return self.__month

    def get_day_name(self)->str:
        """
        Retorna el nombre del dia actual.
        """
        return self.DAY_NAMES_TUPLE\
            [self.__day]
    
    def get_cycle_year_name(self)->str:
        """
        Obtiene el nombre del ciclo del
        año actual.
        """
        n = self.__cycle_year
        return DateAsp\
            .YEARS_CYCLE_NAMES_TUPLE[n]

    def get_month_name(self)->str:
        """
        Retorna el nombre del mes actual.
        """
        return self.MONTH_NAMES_TUPLE\
            [self.__month]

    def advance_one_day(self):
        """
        Funcion que avansa un dia en el
        tiempo del calendario del
        simulador.
        """
        self.__day += 1
        self.__day_code += 1
        if(self.__day == self\
                .DAYS_BY_MONTH):
            self.__day = 0
            self.__month += 1
        if(self.__month == self\
                .MONTHS_BY_YEAR):
            self.__month = 0
            self.__year += 1
            self.__day_code = 0
            self.__cycle_year += 1
        max_years = self\
            .get_years_by_cycle_year()
        if(max_years == self.__cycle_year):
            self.__cycle_year = 0
            