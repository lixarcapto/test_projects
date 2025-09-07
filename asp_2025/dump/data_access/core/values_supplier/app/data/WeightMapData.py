



from basic.Basic import Basic

class WeightMapData:

    def __init__(self):
        array = [
            "in_the_bones",
            "malnutrited",
            "thin",
            "in_shape",
            "fat",
            "obese",
            "morbid"
        ]
        self.INNER = Basic().convertArrayToMap(array)
