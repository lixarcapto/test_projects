

import random
from data_access.DataAccess import DataAccess

class DataGenerator:

    """
        Generacion de valores aleatorios de cualquier tipo.
    """

    def __init__(self):
        return

    def generateNameOfRegion(self, cultureCode):
        regionNamesMatrix = DataAccess().getNamesData().getRegionNamesMatrix()
        nameArray = regionNamesMatrix[cultureCode]
        randomInt = random.randint(0, len(nameArray) -1)
        return nameArray[randomInt]

    def generateRaceByCulture(self, culture):
        raceKey = 0
        array = None
        racesByCulture = DataAccess().getRacesByCultureData()
        array = racesByCulture.RACES_BY_CULTURE_ARRAY[culture]
        raceKey = random.randint(0, len(array) -1)
        return array[raceKey]
