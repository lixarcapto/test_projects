


from data_model.app.body_lib.core.race.app.product.RaceProduct import RaceProduct

class RaceSlavsProduct(RaceProduct):

    def __init__(self):
        super().__init__()
        self.keyCode = self.PERSON_KEYS.RACE.SLAVS
        self.heightPosibleArray = [
            self.PERSON_KEYS.HEIGHT.GIANT,
            self.PERSON_KEYS.HEIGHT.TALL
        ]
        self.hairColorPosibleArray = [
            self.PERSON_KEYS.HAIR_COLOR.BROWN,
            self.PERSON_KEYS.HAIR_COLOR.REDHEAD
        ]
        self.eyeTypePosibleArray = [
            self.PERSON_KEYS.EYE_TYPE.ROUND,
            self.PERSON_KEYS.EYE_TYPE.DROOPY
        ]
        self.skinColorPosibleArray = [
            self.PERSON_KEYS.SKIN_COLOR.BEIGE,
            self.PERSON_KEYS.SKIN_COLOR.OLIVE,
            self.PERSON_KEYS.SKIN_COLOR.SAND
        ]
        self.eyeColorPosibleArray = [
            self.PERSON_KEYS.EYE_COLOR.BROWN,
            self.PERSON_KEYS.EYE_COLOR.SKYBLUE,
            self.PERSON_KEYS.EYE_COLOR.GREEN
        ]
