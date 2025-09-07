

class AgePack:

    def __init__(self):
        self._daysOld = 0
        self._monthsOld = 0
        self._yearsOld = 0
        self._actualAge = 0
        return

    def setDaysOld(self, vint):
        self._daysOld = vint

    def getDaysOld(self):
        return self._daysOld

    def setMonthsOld(self, vint):
        self._monthsOld = vint

    def getMonthsOld(self):
        return self._monthsOld

    def setYearsOld(self, vint):
        self._yearsOld = vint

    def getYearsOld(self):
        return self._yearsOld

    def setActualAge(self, vint):
        self._actualAge = vint

    def getActualAge(self):
        return self._actualAge
