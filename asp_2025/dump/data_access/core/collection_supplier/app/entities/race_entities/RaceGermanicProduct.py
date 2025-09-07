



from data_model.app.body_lib.core.race.app.product.RaceProduct import RaceProduct

class RaceGermanicProduct(RaceProduct):

    def __init__(self):
        super().__init__()
        self.keyCode = self.PERSON_KEYS.RACE.GERMANIC
        self.heightPosibleArray = [
            self.PERSON_KEYS.HEIGHT.GIANT,
            self.PERSON_KEYS.HEIGHT.TALL,
            self.PERSON_KEYS.HEIGHT.MIDDLE
        ]
        self.hairColorPosibleArray = [
            self.PERSON_KEYS.HAIR_COLOR.REDHEAD,
            self.PERSON_KEYS.HAIR_COLOR.BLONDE,
            self.PERSON_KEYS.HAIR_COLOR.BROWN
        ]
        self.eyeTypePosibleArray = [
            self.PERSON_KEYS.EYE_TYPE.ROUND,
            self.PERSON_KEYS.EYE_TYPE.DROOPY
        ]
        self.skinColorPosibleArray = [
            self.PERSON_KEYS.SKIN_COLOR.PALE,
            self.PERSON_KEYS.SKIN_COLOR.WHITE,
            self.PERSON_KEYS.SKIN_COLOR.BEIGE
        ]
        self.eyeColorPosibleArray = [
            self.PERSON_KEYS.EYE_COLOR.BLUE,
            self.PERSON_KEYS.EYE_COLOR.SKYBLUE,
            self.PERSON_KEYS.EYE_COLOR.BLACK,
            self.PERSON_KEYS.EYE_COLOR.BROWN
        ]
