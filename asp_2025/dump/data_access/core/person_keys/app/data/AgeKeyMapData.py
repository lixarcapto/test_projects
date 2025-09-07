



from basic.Basic import Basic

class AgeKeyMapData:

    def __init__(self):
        array = [
            "baby",
            "child",
            "teen",
            "young",
            "young_adult",
            "adult",
            "senior",
            "elder",
            "dying",
            "not dead"
        ]
        self.INNER = Basic().convertArrayToMap(array)
        return
