



import datetime
from ....btpy_string.mod.divide_string.divide_string import*
from datetime import date, timedelta

class Date:

    MONTHS_NAMES_TUPLE:tuple[str] = (
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    )

    DAYS_NAMES_TUPLE:tuple[str] = (
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    )

    def __init__(self, DAY:int, 
            MONTH:int, YEAR:int):
        self.date = None
        self.set_date(
            DAY, 
            MONTH,
            YEAR
        )

    def get_months_names(self)->tuple[str]:
        return Date.MONTHS_NAMES_TUPLE
    
    def get_days_names(self)->tuple[str]:
        return Date.DAYS_NAMES_TUPLE

    def get_date_time(self)->datetime.date:
        return self.date

    def set_date_time(self, 
            date_time:datetime.date):
        self.date = date_time

    def get_actual_date(self)\
            ->datetime.date:
        return datetime.date.today()

    def set_date(self, DAY:int, 
            MONTH:int, YEAR:int)->None:
        self.date = datetime.date(
            YEAR, 
            MONTH, 
            DAY
        )

    def set_year(self, YEAR:int)->int:
        self.date = self.date.replace(
            year = YEAR)

    def get_year(self)->int:
        return self.date.year
    
    def set_month(self, MONTH:int):
        self.date = self.date.replace(
            month = MONTH)
    
    def get_month(self)->int:
        return self.date.month
    
    def get_month_number(self, NAME:str):
        index = Date.MONTHS_NAMES_TUPLE\
            .index(NAME)
        return index +1
        
    
    def set_day(self, DAY:int):
        self.date = self.date.replace(
            day = DAY)
    
    def get_day(self)->int:
        return self.date.day
    
    def get_numeric_british_date(self)->str:
        return self.date.strftime(
            "%d/%m/%Y")
    
    def __str__(self):
        return self.get_numeric_british_date()
    
    def __get_ordinal_number(self, 
            NUMBER:int):
        return Date.ORDINAL_NUMBER_TUPLE\
            [NUMBER]
    
    def get_numeric_american_date(self)\
            ->str:
        return f"{self.get_month()}/"\
            + f"{self.get_day()}/"\
            + f"{self.get_year()}"
    
    def get_month_name(self)->str:
        return Date.MONTHS_NAMES_TUPLE\
            [self.get_month() -1]
    
    def get_day_name(self)->str:
        return Date.DAYS_NAMES_TUPLE\
            [self.get_day() -1]
    
    def get_american_date(self)->str:
        return ""\
            + str(self.get_month_name())\
            + f" {self.get_day()}th, "\
            + str(self.get_year())
        
    def get_british_date(self)->str:
        return ""\
            + f"{self.get_day()}th of "\
            + str(self.get_month_name())\
            + " " + str(self.get_year())
    
    def convert_to_days(self)->int:
        days = 0
        days += self.get_day()
        days += self.get_month() * 4 * 7
        days += self.get_year() \
            * 12 * 4 * 7
        return days