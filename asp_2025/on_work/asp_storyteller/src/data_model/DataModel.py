


from data_model.core.society.Society import Society
from data_model.core.market.Market import Market
from data_model.core.date.Date import Date

class DataModel:

    def __init__(self):
        self.date = Date()
        self.market = Market()
        self.society = Society()
        return

    def createNewScenario(self):
        self.society.createRandomSociety("nordic", 10)

    def writeCitizenInformation(self):
        text = "world information: "
        text += self.society.writeCitizenInformation()
        return text

    def advanceOneDay(self):
        self.date.advanceOneDay()
        self.market = self.society.advanceOneDay(self.market,
        self.date.writeDate())
