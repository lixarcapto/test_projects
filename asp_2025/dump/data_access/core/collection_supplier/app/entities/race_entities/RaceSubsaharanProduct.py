



from data_model.app.body_lib.core.race.app.product.RaceProduct import RaceProduct

class RaceSubsaharanProduct(RaceProduct):

    def __init__(self):
        super().__init__()
        self.keyCode = self.PERSON_KEYS.RACE.SUBSAHARAN
        self.heightPosibleArray = [
            self.PERSON_KEYS.HEIGHT.MIDDLE,
            self.PERSON_KEYS.HEIGHT.DWARF,
            self.PERSON_KEYS.HEIGHT.LOW
        ]
        self.hairColorPosibleArray = [
            self.PERSON_KEYS.HAIR_COLOR.BLACK,
            self.PERSON_KEYS.HAIR_COLOR.BROWN
        ]
        self.eyeTypePosibleArray = [
            self.PERSON_KEYS.EYE_TYPE.ROUND,
            self.PERSON_KEYS.EYE_TYPE.NUTTY,
            self.PERSON_KEYS.EYE_TYPE.SEPARATED
        ]
        self.skinColorPosibleArray = [
            self.PERSON_KEYS.SKIN_COLOR.BLACK,
            self.PERSON_KEYS.SKIN_COLOR.BROWN,
            self.PERSON_KEYS.SKIN_COLOR.LIGHT_BROWN,
            self.PERSON_KEYS.SKIN_COLOR.GRAY
        ]
        self.eyeColorPosibleArray = [
            self.PERSON_KEYS.EYE_COLOR.BROWN,
            self.PERSON_KEYS.EYE_COLOR.BLACK
        ]
