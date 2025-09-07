


from data_access.DataAccess import DataAccess

class Date:

    DAYS_LIMIT_BY_WEEK = 3
    WEEKS_LIMIT_BY_MONTH = 1
    MONTHS_LIMIT_BY_YEAR = 3
    YEARS_LIMIT_BY_ERA = 4

    def __init__(self):
        self._day = 0
        self._week = 0
        self._month = 0
        self._year = 0
        self._numberDay = 0

    #MODIFIER ----------------------------------------------------------------------------------------

    def calculateTheDateByAdding(self, numberOfDays):
        return

    def writeDate(self):
        translator = DataAccess().createTranslator()
        text = ""
        text += " el " + translator.obtainDayName(self.getDay())
        text += " " + str(self.getNumberDay())
        text += " de " + translator.obtainMonthName(self.getMonth())
        text += " del año " + str(self.getYear()) + " d.c "
        return text

    def advanceOneDay(self):
        numberDay = self.getNumberDay() + 1
        self.setNumberDay(numberDay)
        day = self.getDay() + 1
        self.setDay(day)
        if(self.getDay() == Date.DAYS_LIMIT_BY_WEEK +1):
            self.setDay(0)
            week = self.getWeek() + 1
            self.setWeek(week)
        if(self.getWeek() == Date.WEEKS_LIMIT_BY_MONTH +1):
            self.setWeek(0)
            month = self.getMonth() + 1
            self.setMonth(month)
        if(self.getMonth() == Date.MONTHS_LIMIT_BY_YEAR +1):
            self.setMonth(0)
            self.setNumberDay(1)
            year = self.getYear() + 1
            self.setYear(year)

    def isEquivalentTo(self, date):
        if(date.getDay() != self.getDay()):
            return False
        if(date.getMonth() != self.getMonth()):
            return False
        return True

    #GETTERS SETTERS--------------------------------------------------------------------------------

    def getDay(self):
        return self._day

    def setDay(self, valueInt):
        self._day = valueInt

    def getWeek(self):
        return self._week

    def setWeek(self, week):
        self._week = week

    def getMonth(self):
        return self._month

    def setMonth(self, month):
        self._month = month

    def getYear(self):
        return self._year

    def setYear(self, year):
        self._year = year

    def getNumberDay(self):
        return self._numberDay

    def setNumberDay(self, numberDay):
        self._numberDay = numberDay

    #--------------------------------------------------------------------------------------
