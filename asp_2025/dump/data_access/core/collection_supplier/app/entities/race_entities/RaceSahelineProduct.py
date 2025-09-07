



from data_model.app.body_lib.core.race.app.product.RaceProduct import RaceProduct

class RaceSahelineProduct(RaceProduct):

    def __init__(self):
        super().__init__()
        self.keyCode = self.PERSON_KEYS.RACE.SAHELINE
        self.heightPosibleArray = [
            self.PERSON_KEYS.HEIGHT.MIDDLE
        ]
        self.hairColorPosibleArray = [
            self.PERSON_KEYS.HAIR_COLOR.BLACK
        ]
        self.eyeTypePosibleArray = [
            self.PERSON_KEYS.EYE_TYPE.ROUND,
            self.PERSON_KEYS.EYE_TYPE.ASIAN,
            self.PERSON_KEYS.EYE_TYPE.NUTTY
        ]
        self.skinColorPosibleArray = [
            self.PERSON_KEYS.SKIN_COLOR.BLACK,
            self.PERSON_KEYS.SKIN_COLOR.LIGHT_BROWN
        ]
        self.eyeColorPosibleArray = [
            self.PERSON_KEYS.EYE_COLOR.BLACK,
            self.PERSON_KEYS.EYE_COLOR.BROWN
        ]
