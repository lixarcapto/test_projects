


from data_model.core.citizen.Citizen import Citizen
from data_model.core.race_collection.RaceCollection import RaceCollection

class Society:

    lastCitizenCode = 0

    def __init__(self):
        self.citizenArray = []
        return

    def writeCitizenInformation(self):
        text = ""
        for citizen in self.citizenArray:
            text += citizen.writeUpdate()
            text += "\n"
        return text

    def advanceOneDay(self, market, dateWritted):
        for citizen in self.citizenArray:
            market = citizen.advanceOneDay(market, dateWritted)
        return market

    def createRandomSociety(self, culture, quantity):
        citizen = None
        race = RaceCollection().getRace(culture)
        for i in range(quantity):
            citizen = self.createCitizen()
            citizen.inner.traitsMap["culture"] = culture
            citizen.applyRaceTraits(race)
            self.addCitizen(citizen)

    def obtainLastCitizenCode(self):
        result = Society.lastCitizenCode
        Society.lastCitizenCode += 1
        return result

    def createCitizen(self):
        citizen = Citizen()
        citizen.inner.setCodeInt(self.obtainLastCitizenCode())
        return citizen

    def addCitizen(self, citizen):
        self.citizenArray.append(citizen)

    def hasCitizen(self):
        for i in range(self.citizenArray.len()):
            if(self.citizenArray[i].inner.getCodeInt() == codeInt):
                if(self.citizenArray[i].inner.getCodeInt()):
                    return True
        return False

    def getCitizenByCode(self, codeInt):
        for i in range(self.citizenArray.len()):
            if(self.citizenArray[i].inner.getCodeInt() == codeInt):
                return self.citizenArray[i]

    def setCitizen(self, citizen):
        codeUpdate = citizen.inner.codeInt()
        for i in range(self.citizenArray.len()):
            if(self.citizenArray[i].inner.getCodeInt() == codeUpdate):
                self.citizenArray[i] = citizen
