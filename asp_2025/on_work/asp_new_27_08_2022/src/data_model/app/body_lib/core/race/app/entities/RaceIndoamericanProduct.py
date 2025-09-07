



from data_model.app.body_lib.core.race.app.product.RaceProduct import RaceProduct

class RaceIndoamericanProduct(RaceProduct):

    def __init__(self):
        super().__init__()
        self.keyCode = self.PERSON_KEYS.RACE.INDOAMERICAN
        self.heightPosibleArray = [
            self.PERSON_KEYS.HEIGHT.LOW,
            self.PERSON_KEYS.HEIGHT.DWARF
        ]
        self.hairColorPosibleArray = [
            self.PERSON_KEYS.HAIR_COLOR.BLACK
        ]
        self.eyeTypePosibleArray = [
            self.PERSON_KEYS.EYE_TYPE.NUTTY,
            self.PERSON_KEYS.EYE_TYPE.ASIAN
        ]
        self.skinColorPosibleArray = [
            self.PERSON_KEYS.SKIN_COLOR.ALMOND,
            self.PERSON_KEYS.SKIN_COLOR.REDDISH
        ]
        self.eyeColorPosibleArray = [
            self.PERSON_KEYS.EYE_COLOR.BLACK,
            self.PERSON_KEYS.EYE_COLOR.BROWN
        ]
