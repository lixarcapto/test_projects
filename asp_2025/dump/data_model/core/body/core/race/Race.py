

from data_model.core.body.core.race.app.product.RaceProduct import RaceProduct

class Race:

    def __init__(self):
        self.inner = RaceProduct()

    def convertMatrixToRace(self, map):
        self.inner.hairColorPosibleArray = map["hair_color"]
        self.inner.eyeTypePosibleArray = map["eye_type"]
        self.inner.heightPosibleArray = map["height"]
        self.inner.skinColorPosibleArray = map["skin_color"]
        self.inner.eyeColorPosibleArray = map["eye_color"]
