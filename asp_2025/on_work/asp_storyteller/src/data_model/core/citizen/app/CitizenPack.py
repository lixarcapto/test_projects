


from data_model.core.age.Age import Age
from basic.Basic import Basic

class CitizenPack:

    initialNeeds = 4

    def __init__(self):
        # personal data
        self.notificationArray = []
        self._name = "none_name"
        self._secondName = "none_second_name"
        self._lastname = "none_lastname"
        self._secondLastname = "none_second_lastname"
        self._nickname = "none_nickname"
        self.age = Age()
        self._culture = 0
        self._religion = 0
        self._lenguage = 0
        self._writing = 0
        self._socialCaste = 0
        self._socialClass = 0
        self._race = 0
        self._sexualOrientation = 0
        self._profession = 0
        self._codeInt = 0
        # rasgos fisicos
        self._skinColor = 0
        self._eyeColor = 0
        self._eyeType = 0
        self._heightMaximum = 0
        self._heightActual = 0
        self._hairType = 0
        self._hairColor = 0
        self._hairLength = 0
        self._appearance = 0
        self._hasFreckles = False
        self.eventQueue = []
        self.history = []
        self.traitsMap = dict()
        # barras vitales
        self.barMap = dict()
        return

    def addTraits(self):
        map = dict()
        self.traitsMap = None
        map["name"] = "name"
        map["second_name"] = "second_name"
        map["lastname"] = "lastname"
        map["second_lastname"] = "second_lastname"
        map["nickname"] = "nickname"
        map["culture"] = "none"
        map["religion"] = "none"
        map["lenguage"] = "none"
        map["writing"] = "none"
        map["gender"] = "he"
        map["social_caste"] = 0
        map["social_class"] = 0
        map["race"] = "none"
        map["sexual_orientation"] = "none"
        map["profession"] = "none"
        map["code_int"] = 0
        map["skin_color"] = "none"
        map["eye_color"] = "none"
        map["eye_type"] = "none"
        map["height_maximum"] = 0
        map["height_actual"] = 0
        map["hair_type"] = "none"
        map["hair_color"] = "none"
        map["hair_length"] = 0
        map["appearance"] = 0
        map["has_freckles"] = False
        self.traitsMap = map

    def addNeedsBars(self):
        array = [
            # barras vitales
            "vision",
            "loyalty",
            "mobility",
            "breathing",
            "handling",
            "musculature",
            "consciense",
            "speech",
            "hearing",
            "aging",
            "scars",
            # Barras nesesidades
            "funeral_services",
            "care",
            "motivation",
            "stress",
            "madness",
            "luck",
            "organic_damage",
            "feed",
            "hydration",
            "blood_lost",
            "open_wound",
            "poisoning_treatment",
            "lesion_treatment",
            "pain_treatment",
            "infection_treatment",
            "virus_treatment",
            "flu_shot",
            "lices_treatment",
            "worms_treatment",
            "plague_shot",
            "allergy_treatment",
            "malaria_treatment",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        self.barMap = Basic().createMapOfInt(array, 0)

    def setName(self, vstring):
        self._name = vstring

    def getName(self):
        return self._name

    def setSecondname(self, vstring):
        self._secondName = vstring

    def getSecondname(self):
        return self._secondName

    def setLastname(self, vstring):
        self._lastname = vstring

    def getLastname(self):
        return self._lastname

    def setSecondLastname(self, vstring):
        self._secondLastname = vstring

    def getSecondLastname(self):
        return self._secondLastname

    def setNickname(self, vstring):
        self._nickname = vstring

    def getNickname(self):
        return self._nickname

    def setCodeInt(self, vint):
        self._codeInt = vint

    def getCodeInt(self):
        return self._codeInt
