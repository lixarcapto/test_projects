



from basic.Basic import Basic

class HeightMapData:

    def __init__(self):
        array = [
            "tiny",
            "little",
            "dwarf",
            "low",
            "middle",
            "tall",
            "giant"
        ]
        self.INNER = Basic().convertArrayToMap(array)
