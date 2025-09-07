


from data_access.core.person_keys.app.data.AgeKeyMapData import AgeKeyMapData
from data_access.core.person_keys.app.data.EyeColorMapData import EyeColorMapData
from data_access.core.person_keys.app.data.EyeTypeMapData import EyeTypeMapData
from data_access.core.person_keys.app.data.FacialHairStyleKeyMapData import FacialHairStyleKeyMapData
from data_access.core.person_keys.app.data.HairColorMapData import HairColorMapData
from data_access.core.person_keys.app.data.HairStyleKeyMapData import HairStyleKeyMapData
from data_access.core.person_keys.app.data.HeightMapData import HeightMapData
from data_access.core.person_keys.app.data.MoodMapData import MoodMapData
from data_access.core.person_keys.app.data.RaceKeyMapData import RaceKeyMapData
from data_access.core.person_keys.app.data.SexualOrientationMapData import SexualOrientationMapData
from data_access.core.person_keys.app.data.SkinColorMapData import SkinColorMapData
from data_access.core.person_keys.app.data.WeightMapData import WeightMapData
from data_access.core.person_keys.app.data.TopicKeysMapData import TopicKeysMapData
from data_access.core.person_keys.app.data.CauseSensationKeysMapData import CauseSensationKeysMapData
from data_access.core.person_keys.app.data.OrganTypeMapData import OrganTypeMapData


class PersonKeys:

    def __init__(self):
        return

    def getAgeKeyMap(self):
        return AgeKeyMapData().INNER

    def getEyeColorMap(self):
        return EyeColorMapData().INNER

    def getEyeTypeMap(self):
        return EyeTypeMapData().INNER

    def getFacialHairStyleKeyMap(self):
        return FacialHairStyleKeyMapData().INNER

    def getHairColorMap(self):
        return HairColorMapData().INNER

    def getHairStyleKeyMap(self):
        return HairStyleKeyMapData().INNER

    def getHeightMap(self):
        return HeightMapData().INNER

    def getMoodMap(self):
        return MoodMapData().INNER

    def getRaceKeyMap(self):
        return RaceKeyMapData().INNER

    def getSexualOrientationMap(self):
        return SexualOrientationMapData().INNER

    def getSkinColorMap(self):
        return SkinColorMapData().INNER

    def getWeightMap(self):
        return WeightMapData().INNER

    def getTopicKeysMap(self):
        return TopicKeysMapData().INNER

    def getCauseSensationKeysMap(self):
        return CauseSensationKeysMapData().INNER

    def getOrganTypeMap(self):
        return OrganTypeMapData().INNER
