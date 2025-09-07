



from data_model.app.body_lib.core.race.app.product.RaceProduct import RaceProduct

class RaceTurkishProduct(RaceProduct):

    def __init__(self):
        super().__init__()
        self.keyCode = self.PERSON_KEYS.RACE.TURKISH
        self.heightPosibleArray = [
            self.PERSON_KEYS.HEIGHT.MIDDLE
        ]
        self.hairColorPosibleArray = [
            self.PERSON_KEYS.HAIR_COLOR.BLACK,
            self.PERSON_KEYS.HAIR_COLOR.BLONDE
        ]
        self.eyeTypePosibleArray = [
            self.PERSON_KEYS.EYE_TYPE.ASIAN,
            self.PERSON_KEYS.EYE_TYPE.NUTTY
        ]
        self.skinColorPosibleArray = [
            self.PERSON_KEYS.SKIN_COLOR.PALE,
            self.PERSON_KEYS.SKIN_COLOR.WHITE,
            self.PERSON_KEYS.SKIN_COLOR.BEIGE,
            self.PERSON_KEYS.SKIN_COLOR.SAND,
            self.PERSON_KEYS.SKIN_COLOR.ALMOND
        ]
        self.eyeColorPosibleArray = [
            self.PERSON_KEYS.EYE_COLOR.BROWN,
            self.PERSON_KEYS.EYE_COLOR.BLACK,
            self.PERSON_KEYS.EYE_COLOR.GREEN
        ]
