



from data_model.app.body_lib.core.race.app.product.RaceProduct import RaceProduct

class RaceMongolianProduct(RaceProduct):

    def __init__(self):
        super().__init__()
        self.keyCode = self.PERSON_KEYS.RACE.MONGOLIAN
        self.heightPosibleArray = [
            self.PERSON_KEYS.HEIGHT.MIDDLE,
            self.PERSON_KEYS.HEIGHT.LOW,
            self.PERSON_KEYS.HEIGHT.DWARF
        ]
        self.hairColorPosibleArray = [
            self.PERSON_KEYS.HAIR_COLOR.BLACK
        ]
        self.eyeTypePosibleArray = [
            self.PERSON_KEYS.EYE_TYPE.SEPARATED
        ]
        self.skinColorPosibleArray = [
            self.PERSON_KEYS.SKIN_COLOR.ALMOND,
            self.PERSON_KEYS.SKIN_COLOR.SAND
        ]
        self.eyeColorPosibleArray = [
            self.PERSON_KEYS.EYE_COLOR.BLACK,
            self.PERSON_KEYS.EYE_COLOR.BROWN
        ]
