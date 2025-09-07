




from basic.Basic import Basic

class OrganTypeMapData:

    def __init__(self):
        array = [
            "circulatory",
            "higher_digestive",
            "nervous",
            "brain",
            "respiratory",
            "endocrine",
            "excretory",
            "lower_digestive",
            "skin",
            "mouth",
            "voice",
            "vision",
            "legs",
            "arms",
            "audition",
            "bone",
            "muscular",
            "reproductive",
            "olfactory",
            "middle_digestive",
            "neck"
        ]
        self.INNER = Basic().convertArrayToMap(array)
        return
