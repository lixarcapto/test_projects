

from data_model.core.race.Race import Race

class RaceExample(Race):

    def __init__(self):
        super().__init__()
        self.keyName = ""
        self.inner.skinColorArray = [""]
        self.inner.eyeColorArray = [""]
        self.inner.eyeTypeArray = [""]
        self.inner.heightMaximumArray = [""]
        self.inner.hairTypeArray = [""]
        self.inner.hairColorArray = [""]
        return
