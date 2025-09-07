


import random
from data_model.app.body_lib.core.race.app.entities.RaceCollectionData import RaceCollectionData

class RandomizeCultureTraitsTk:

    def __init__(self):
        self.RACE_COLLECTION = RaceCollectionData()

    def selectRandomFromArray(self, array):
        if(1 < len(array)):
            return array[random.randint(0, len(array) -1)]
        else:
            return array[0]

    def inner(self, bodyProduct):
        randomValue = 0
        raceProduct = self.RACE_COLLECTION.culturesArray[bodyProduct.getRace()]
        bodyProduct.setHairColor(self.selectRandomFromArray(raceProduct.hairColorPosibleArray))
        bodyProduct.setEyeType(self.selectRandomFromArray(raceProduct.eyeTypePosibleArray))
        bodyProduct.setLimitHeight(self.selectRandomFromArray(raceProduct.heightPosibleArray))
        bodyProduct.setSkinColor(self.selectRandomFromArray(raceProduct.skinColorPosibleArray))
        bodyProduct.setEyeColor(self.selectRandomFromArray(raceProduct.eyeColorPosibleArray))
        return bodyProduct
