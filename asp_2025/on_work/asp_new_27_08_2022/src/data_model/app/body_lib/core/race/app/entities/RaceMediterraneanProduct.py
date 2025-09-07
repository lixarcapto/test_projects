


from data_model.app.body_lib.core.race.app.product.RaceProduct import RaceProduct

class RaceMediterraneanProduct(RaceProduct):

    def __init__(self):
        super().__init__()
        self.keyCode = self.PERSON_KEYS.RACE.MEDITERRANEAN
        self.heightPosibleArray = [
            self.PERSON_KEYS.HEIGHT.TALL,
            self.PERSON_KEYS.HEIGHT.MIDDLE,
            self.PERSON_KEYS.HEIGHT.LOW
        ]
        self.hairColorPosibleArray = [
            self.PERSON_KEYS.HAIR_COLOR.BLACK,
            self.PERSON_KEYS.HAIR_COLOR.BROWN
        ]
        self.eyeTypePosibleArray = [
            self.PERSON_KEYS.EYE_TYPE.ROUND,
            self.PERSON_KEYS.EYE_TYPE.DROOPY
        ]
        self.skinColorPosibleArray = [
            self.PERSON_KEYS.SKIN_COLOR.WHITE,
            self.PERSON_KEYS.SKIN_COLOR.BEIGE,
            self.PERSON_KEYS.SKIN_COLOR.OLIVE
        ]
        self.eyeColorPosibleArray = [
            self.PERSON_KEYS.EYE_COLOR.BLACK,
            self.PERSON_KEYS.EYE_COLOR.BROWN,
            self.PERSON_KEYS.EYE_COLOR.LIGHT_BROWN
        ]
