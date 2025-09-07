

from data_model.app.market_lib.core.title.Title import Title

class MarketLocal:

    def __init__(self):
        self.titlesArray = []

    def setTitle(self, title):
        return

    def addTitle(self, regionCode, terrainCode):
        titles = Title()
        titles.regionCode = regionCode
        titles.terrainCode = terrainCode
        self.titlesArray.append(titles)

    def getTitle(self, regionCode, terrainCode):
        return

    def extractTitle(self, regionCode, terrainCode):
        return
