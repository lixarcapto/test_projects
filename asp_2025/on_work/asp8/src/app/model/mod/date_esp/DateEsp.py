


from .mod.DATE_ESP_CONST import*

class DateEsp:

    """
     Clases dedicada a la manipulación 
     de fechas especiales para el 
     programa
    """

    DAY_LIMIT = 3
    SEASON_LIMIT = 4
    WEEK_LIMIT = 2

    def __init__(self) -> None:
        self.day = 0
        self.day_number = 0
        self.week = 0
        self.season = 0
        self.year = 0

    def get_day_text(self):
        return DAY_ARRAY[self.day]
    
    def get_season_text(self):
        return SEASON_ARRAY[self.season]

    def write_narrative(self):
        txt = ""
        txt += f"{self.get_day_text()} "
        txt += f"{self.day_number + 1}, "
        txt += f"{self.get_season_text()} "
        txt += f" {self.week + 1}st, "
        txt += f" {self.year + 1}."
        return txt

    def one_more_day(self):
        self.day += 1
        self.day_number += 1
        if(self.day == DateEsp.DAY_LIMIT):
            self.day = 0
            self.week += 1
        if(self.week == DateEsp.WEEK_LIMIT):
            self.week = 0
            self.season += 1
            self.day_number = 0
        if(self.season == DateEsp.SEASON_LIMIT):
            self.season = 0
            self.year += 1