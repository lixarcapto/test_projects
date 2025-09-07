


from data_access.core.translator.app.NamesData import NamesData

class Translator:

    def __init__(self):
        return

    def obtainAgeName(self, vint):
        namesData = NamesData()
        return namesData.ageNamesArray[vint]

    def obtainMonthName(self, vint):
        return NamesData().monthsNamesArray[vint]

    def obtainDayName(self, vint):
        return NamesData().daysNamesArray[vint]
