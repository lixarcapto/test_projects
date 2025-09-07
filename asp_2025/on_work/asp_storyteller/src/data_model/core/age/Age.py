

from data_model.core.age.app.AgePack import AgePack
from data_access.DataAccess import DataAccess

class Age:

    def __init__(self):
        self.inner = AgePack()
        return

    def advanceOneDay(self):
        self.inner.setDaysOld(self.inner.getDaysOld() + 1)
        if(self.inner.getDaysOld() >= 3):
            self.inner.setMonthsOld(self.inner.getMonthsOld() + 1)
            self.inner.setDaysOld(0)
        if(self.inner.getMonthsOld() >= 3):
            self.inner.setYearsOld(self.inner.getYearsOld() + 1)
            self.inner.setMonthsOld(0)

    def writeAge(self):
        text = ""
        translator = DataAccess().getTranslator()
        vint = self.inner.getActualAge()
        text += translator.obtainAgeName(vint) + " "
        text += str(self.inner.getYearsOld()) + " years "
        text += str(self.inner.getMonthsOld()) + " months "
        text += str(self.inner.getDaysOld()) + " days old "
        return text
