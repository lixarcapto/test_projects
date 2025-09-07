


from data_model.app.body_lib.core.race.app.product.RaceProduct import RaceProduct

class RaceAsianProduct(RaceProduct):

    def __init__(self):
        super().__init__()
        self.keyCode = self.PERSON_KEYS.RACE.ASIAN
        self.heightPosibleArray = [
            self.PERSON_KEYS.HEIGHT.MIDDLE
        ]
        self.hairColorPosibleArray = [
            self.PERSON_KEYS.HAIR_COLOR.BLACK
        ]
        self.eyeTypePosibleArray = [
            self.PERSON_KEYS.EYE_TYPE.ASIAN,
            self.PERSON_KEYS.EYE_TYPE.SEPARATED
        ]
        self.skinColorPosibleArray = [
            self.PERSON_KEYS.SKIN_COLOR.SAND,
            self.PERSON_KEYS.SKIN_COLOR.OLIVE,
            self.PERSON_KEYS.SKIN_COLOR.ALMOND
        ]
        self.eyeColorPosibleArray = [
            self.PERSON_KEYS.EYE_COLOR.BROWN
        ]
