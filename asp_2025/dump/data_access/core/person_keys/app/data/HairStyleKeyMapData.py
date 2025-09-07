



from basic.Basic import Basic

class HairStyleKeyMapData:

    def __init__(self):
        array = [
            "bald_head",
            "shave_head",
            "butch_hair",
            "short_hair",
            "tousled_hair",
            "shoulder_length_hair",
            "long_hair",
            "hair_down_to_feet",
            "princess_hair"
        ]
        self.INNER = Basic().convertArrayToMap(array)
