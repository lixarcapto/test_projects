

from basic.Basic import Basic

class ApplyRaceTraitsTask:

    def inner(self, citizenPack, race):
        vstring = ""
        vstring = Basic().randomizeElementFromArray(race.inner.skinColorArray)
        citizenPack.traitsMap["skin_color"] = vstring
        vstring = Basic().randomizeElementFromArray(race.inner.eyeColorArray)
        citizenPack.traitsMap["eye_color"] = vstring
        vstring = Basic().randomizeElementFromArray(race.inner.skinColorArray)
        citizenPack.traitsMap["eye_type"] = vstring
        vstring = Basic().randomizeElementFromArray(race.inner.heightMaximumArray)
        citizenPack.traitsMap["height_maximum"] = vstring
        vstring = Basic().randomizeElementFromArray(race.inner.skinColorArray)
        citizenPack.traitsMap["skin_color"] = vstring
        vstring = Basic().randomizeElementFromArray(race.inner.hairTypeArray)
        citizenPack.traitsMap["hair_type"] = vstring
        vstring = Basic().randomizeElementFromArray(race.inner.hairColorArray)
        citizenPack.traitsMap["hair_color"] = vstring
        return citizenPack
