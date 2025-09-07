



from basic.Basic import Basic

class SexualOrientationMapData:

    def __init__(self):
        array = [
            "heterosexual",
            "homosexual",
            "bisexual",
            "asexual",
            "childs",
            "sadistic",
            "beast",
            "dead"
        ]
        self.INNER = Basic().convertArrayToMap(array)
