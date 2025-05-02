




class DateManagerData:

    """
        Clase que contiene los datos de una fecha.
    """

    NUMBER_DAYS = 7
    NUMBER_WEEKS = 4
    NUMBER_MONTHS = 12
    MONTHS_DAYS_ARRAY = [
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

    def __init__(self):
        self.year = 1
        self.month = 1
        self.week = 1
        self.day = 1
        self.day_of_month = 1
        self.day_of_week = 1

    def is_a_valid_int(self, integer):
        if(not isinstance(integer, int)):
            print("=> Error invalid integer: in DateData.is_a_valid_int")
            return 0
        return integer

    def set_year(self, integer):
        integer = self.is_a_valid_int(integer)
        self.year = integer

    def get_year(self):
        return self.year

    def set_month(self, integer):
        integer = self.is_a_valid_int(integer)
        self.month = integer

    def get_month(self):
        return self.month

    def set_week(self, integer):
        integer = self.is_a_valid_int(integer)
        self.week = integer

    def get_week(self):
        return self.week

    def set_day(self, integer):
        integer = self.is_a_valid_int(integer)
        self.day = integer

    def get_day(self):
        return self.day
