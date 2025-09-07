

from basic.Basic import Basic

class SkinColorMapData:

    def __init__(self):
        array = [
            "pale",
            "white",
            "beige",
            "olive",
            "reddish",
            "almond",
            "light_brown",
            "brown",
            "black",
            "gray",
            "sand"
        ]
        self.INNER = Basic().convertArrayToMap(array)
        return
