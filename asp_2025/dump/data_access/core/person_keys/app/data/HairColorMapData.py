



from basic.Basic import Basic

class HairColorMapData:

    def __init__(self):
        array = [
            "black",
            "brown",
            "blonde",
            "redhead",
            "grey",
            "white"
        ]
        self.INNER = Basic().convertArrayToMap(array)
