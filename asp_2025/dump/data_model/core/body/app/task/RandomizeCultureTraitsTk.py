


import random
from data_model.core.body.app.task.LoadRaceCollectionTK import LoadRaceCollectionTK

class RandomizeCultureTraitsTk:

    def __init__(self):
        loadRaceCollection = LoadRaceCollectionTK()
        self.RACE_COLLECTION = loadRaceCollection.inner()

    def selectRandomFromArray(self, array):
        if(1 < len(array)):
            return array[random.randint(0, len(array) -1)]
        else:
            return array[0]

    def inner(self, bodyProduct):
        randomValue = 0
        raceProduct = self.RACE_COLLECTION[bodyProduct.getRace()]
        genes = bodyProduct.getGenesThis()
        genes.setHairColor(self.selectRandomFromArray(raceProduct.inner.hairColorPosibleArray))
        genes.setEyeType(self.selectRandomFromArray(raceProduct.inner.eyeTypePosibleArray))
        genes.setHeightLimit(self.selectRandomFromArray(raceProduct.inner.heightPosibleArray))
        genes.setSkinColor(self.selectRandomFromArray(raceProduct.inner.skinColorPosibleArray))
        genes.setEyeColor(self.selectRandomFromArray(raceProduct.inner.eyeColorPosibleArray))
        bodyProduct.setGenesThis(genes)
        return bodyProduct
