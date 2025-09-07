

from data_access.app.person.object.PersonSkinColorData import PersonSkinColorData
from data_access.app.person.object.PersonHairColorData import PersonHairColorData
from data_access.app.person.object.PersonEyeTypeData import PersonEyeTypeData
from data_access.app.person.object.PersonEyeColorData import PersonEyeColorData
from data_access.app.person.object.PersonRaceKeyData import PersonRaceKeyData
from data_access.app.person.object.PersonHeightData import PersonHeightData
from data_access.app.person.object.PersonAgeData import PersonAgeData
from data_access.app.person.object.DesitionData import DesitionData
from data_access.app.person.object.EmotionsData import EmotionsData
from data_access.app.person.object.ThoughtsData import ThoughtsData
from data_access.app.person.object.TopicsData import TopicsData
from data_access.app.person.object.PersonSexData import PersonSexData
from data_access.app.person.object.PersonSexualOrientationData import PersonSexualOrientationData
from data_access.app.person.object.PersonValues import PersonValues
from data_access.app.person.object.PersonWeightData import PersonWeightData

class PersonKeysData:

    def __init__(self):
        self.SKIN_COLOR = PersonSkinColorData()
        self.HAIR_COLOR = PersonHairColorData()
        self.EYE_TYPE = PersonEyeTypeData()
        self.EYE_COLOR = PersonEyeColorData()
        self.RACE = PersonRaceKeyData()
        self.HEIGHT = PersonHeightData()
        self.AGE = PersonAgeData()
        self.DESITION = DesitionData()
        self.EMOTION = EmotionsData()
        self.THOUGHT = ThoughtsData()
        self.TOPIC = TopicsData()
        self.VALUES = PersonValues()
        self.SEX = PersonSexData()
        self.ORIENTATION = PersonSexualOrientationData()
        self.WEIGHT = PersonWeightData()
