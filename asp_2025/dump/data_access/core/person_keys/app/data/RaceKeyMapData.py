

from basic.Basic import Basic

class RaceKeyMapData:

    def __init__(self):
        array = [
            "nordic",
            "mediterranean",
            "germanic",
            "celtic",
            "slavs",
            "arab",
            "subsaharan",
            "turkish",
            "mongolian",
            "asian",
            "saheline",
            "polynesian",
            "indoamerican",
            "indian"
        ]
        self.INNER = Basic().convertArrayToMap(array)
        return
