

from data_access.core.person_keys.PersonKeys import PersonKeys

class RaceSlavsMap:

    def __init__(self):
        self.INNER = dict()
        self.INNER["height"] = [
            PersonKeys().getHeightMap()["tall"],
            PersonKeys().getHeightMap()["middle"],
            PersonKeys().getHeightMap()["low"]
        ]
        self.INNER["hair_color"] = [
            PersonKeys().getHairColorMap()["black"]
        ]
        self.INNER["eye_type"] = [
            PersonKeys().getEyeTypeMap()["round"],
            PersonKeys().getEyeTypeMap()["nutty"]
        ]
        self.INNER["skin_color"] = [
            PersonKeys().getSkinColorMap()["olive"],
            PersonKeys().getSkinColorMap()["almond"]
        ]
        self.INNER["eye_color"] = [
            PersonKeys().getEyeColorMap()["black"],
            PersonKeys().getEyeColorMap()["brown"]
        ]
        return
