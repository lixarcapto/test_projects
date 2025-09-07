

class DatePack:

    def __init__(self):
        self._day = 0
        self._month = 0
        self._year = 0
        self._dayNumber = 0
        return

    def getDay(self):
        return self._day

    def setDay(self, vint):
        self._day = vint

    def getMonth(self):
        return self._month

    def setMonth(self, vint):
        self._month = vint

    def getYear(self):
        return self._year

    def setYear(self, vint):
        self._year = vint

    def getDayNumber(self):
        return self._dayNumber

    def setDayNumber(self, vint):
        self._dayNumber = vint
