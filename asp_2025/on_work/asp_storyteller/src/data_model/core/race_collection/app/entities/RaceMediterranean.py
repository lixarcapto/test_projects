

from data_model.core.race.Race import Race

class RaceMediterranean(Race):

    def __init__(self):
        super().__init__()
        self.keyName = "mediterranean"
        self.inner.skinColorArray = ["olive", "beige"]
        self.inner.eyeColorArray = ["black", "dark_brown"]
        self.inner.eyeTypeArray = ["round"]
        self.inner.heightMaximumArray = [5, 4, 3]
        self.inner.hairTypeArray = ["straight", "waby"]
        self.inner.hairColorArray = ["black", "brown"]
        return
