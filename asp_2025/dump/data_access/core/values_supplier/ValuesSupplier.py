



from data_access.core.values_supplier.app.data.PersonCultureMatrixData import PersonCultureMatrixData
from data_access.core.values_supplier.app.data.DesitionMatrixData import DesitionMatrixData
from data_access.core.values_supplier.app.data.EmotionsMatrixData import EmotionsMatrixData
from data_access.core.values_supplier.app.data.PersonAgeMatrixData import PersonAgeMatrixData
from data_access.core.values_supplier.app.data.PersonEyeColorArrayData import PersonEyeColorArrayData
from data_access.core.values_supplier.app.data.PersonEyeTypeArrayData import PersonEyeTypeArrayData
from data_access.core.values_supplier.app.data.PersonHairColorArrayData import PersonHairColorArrayData
from data_access.core.values_supplier.app.data.PersonHeightArrayData import PersonHeightArrayData
from data_access.core.values_supplier.app.data.PersonRaceKeyArrayData import PersonRaceKeyArrayData
from data_access.core.values_supplier.app.data.SexualOrientationArrayData import SexualOrientationArrayData
from data_access.core.values_supplier.app.data.SkinColorArrayData import SkinColorArrayData
from data_access.core.values_supplier.app.data.RacesByCulturesData import RacesByCulturesData
from data_access.core.values_supplier.app.data.HairStyleKeyMapData import HairStyleKeyMapData
from data_access.core.values_supplier.app.data.FacialHairStyleKeyMapData import FacialHairStyleKeyMapData
from data_access.core.values_supplier.app.data.WeightMapData import WeightMapData
from data_access.core.values_supplier.app.data.PersonValues import PersonValues
from basic.Basic import Basic

class ValuesSupplier:

    def __init__(self):
        return

    def getPersonValuesData(self):
        return PersonValues()

    def getCulturesLimit(self):
        return len(PersonCultureMatrixData().INNER)

    def getPersonCultureMap(self):
        personCultureMatrix = PersonCultureMatrixData().INNER
        return Basic().convertMatrixToMap(personCultureMatrix)

    def getDesitionLimit(self):
        return len(DesitionMatrixData().INNER)

    def getDesitionMap(self):
        desitionMatrixData = DesitionMatrixData().INNER
        return Basic().convertMatrixToMap(desitionMatrixData)

    def getEmotionsLimit(self):
        return len(EmotionsMatrixData().INNER)

    def getEmotionsMap(self):
        emotionsMatrixData = EmotionsMatrixData().INNER
        return Basic().convertMatrixToMap(emotionsMatrixData)

    def getAgeLimit(self):
        return len(PersonAgeMatrixData().INNER)

    def getAgeMap(self):
        personAgeMatrixData = PersonAgeMatrixData().INNER
        return Basic().convertMatrixToMap(personAgeMatrixData)

    def getEyeColorLimit(self):
        return len(PersonEyeColorArrayData().INNER)

    def getEyeColorMap(self):
        personEyeColorArrayData = PersonEyeColorArrayData().INNER
        return Basic().convertArrayToMap(personEyeColorArrayData)

    def getEyeTypeLimit(self):
        return len(PersonEyeTypeArrayData().INNER)

    def getEyeTypeMap(self):
        personEyeTypeArrayData = PersonEyeTypeArrayData().INNER
        return Basic().convertArrayToMap(personEyeTypeArrayData)

    def getHairColorLimit(self):
        return len(PersonHairColorArrayData().INNER)

    def getHairColorMap(self):
        personHairColorArrayData = PersonHairColorArrayData().INNER
        return Basic().convertArrayToMap(personHairColorArrayData)

    def getHeightLimit(self):
        return len(PersonHeightArrayData().INNER)

    def getHeightMap(self):
        personHeightArrayData = PersonHeightArrayData().INNER
        return Basic().convertArrayToMap(personHeightArrayData)

    def getRaceKeyLimit(self):
        return len(PersonHeightArrayData().INNER)

    def getRaceKeyMap(self):
        return PersonRaceKeyArrayData().INNER

    def getSexualOrientationLimit(self):
        return len(SexualOrientationArrayData().INNER)

    def getSexualOrientationMap(self):
        sexualOrientationArrayData = SexualOrientationArrayData().INNER
        return Basic().convertArrayToMap(sexualOrientationArrayData)

    def getSexualOrientationLimit(self):
        return len(SexualOrientationArrayData().INNER)

    def getSexualOrientationMap(self):
        sexualOrientationArrayData = SexualOrientationArrayData().INNER
        return Basic().convertArrayToMap(sexualOrientationArrayData)

    def getSkinColorLimit(self):
        return len(SkinColorArrayData().INNER)

    def getSkinColorMap(self):
        skinColorArrayData = SkinColorArrayData().INNER
        return Basic().convertArrayToMap(skinColorArrayData)

    def getFacialHairStyleKeyMapLimit(self):
        return len(FacialHairStyleKeyMapData().INNER)

    def getFacialHairStyleMap(self):
        facialHairStyleKeyMap = FacialHairStyleKeyMapData().INNER
        return Basic().convertArrayToMap(facialHairStyleKeyMap)

    def getHairStyleKeyMapLimit(self):
        return len(HairStyleKeyMapData().INNER)

    def getHairStyleKeyMap(self):
        hairStyleKeyMap = HairStyleKeyMapData().INNER
        return Basic().convertArrayToMap(hairStyleKeyMap)

    def getRacesByCulturesData(self):
        return RacesByCulturesData().INNER

    def getWeightLimit(self):
        return len(WeightMapData().INNER)

    def getWeightMap(self):
        return WeightMapData().INNER
