


from data_model.core.date.app.DatePack import DatePack
from data_access.DataAccess import DataAccess

class Date:

    def __init__(self):
        self.inner = DatePack()
        return

    def writeDate(self):
        text = ""
        translator = DataAccess().getTranslator()
        text += str(self.inner.getDayNumber()) + " "
        vint = self.inner.getMonth()
        text += translator.obtainMonthName(vint) + " "
        vint = self.inner.getDay()
        text += translator.obtainDayName(vint) + " "
        text += str(self.inner.getYear()) + " "
        return text

    def advanceOneDay(self):
        self.inner.setDay(self.inner.getDay() + 1)
        self.inner.setDayNumber(self.inner.getDayNumber() + 1)
        if(self.inner.getDay() >= 3):
            self.inner.setMonth(self.inner.getMonth() + 1)
            self.inner.setDay(0)
        if(self.inner.getMonth() >= 3):
            self.inner.setYear(self.inner.getYear() + 1)
            self.inner.setMonth(0)
            self.inner.setDayNumber(0)
