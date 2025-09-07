

from data_model.core.race.Race import Race

class RaceNordic(Race):

    def __init__(self):
        super().__init__()
        self.keyName = "nordic"
        self.inner.skinColorArray = ["pale", "white"]
        self.inner.eyeColorArray = ["green", "blue"]
        self.inner.eyeTypeArray = ["round"]
        self.inner.heightMaximumArray = [6, 5]
        self.inner.hairTypeArray = ["straight", "waby"]
        self.inner.hairColorArray = ["blonde", "brown"]
        return
