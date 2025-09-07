


from data_model.core.market.Market import Market
from data_access.DataAccess import DataAccess
from data_model.core.nation.app.pack.NationPack import NationPack

class Nation:

    def __init__(self):
        self.inner = NationPack()
        return

    def writeNationData(self):
        text = ""
        keysData = DataAccess().getKeysData()
        finalText = ""
        finalText += "code " + str(self.inner.getCode()) + "\n"
        text = keysData.getCultureKey(self.inner.getCultureCode())
        finalText += "culture: " + text + "\n"
        finalText += "region onwer" + "\n"
        for e in self.inner.getOwnedRegionCodesArray():
            finalText += " >> " + str(e) + "\n"
        return finalText
