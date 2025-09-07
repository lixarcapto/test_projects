


from basic.Basic import Basic

class FacialHairStyleKeyMapData:

    def __init__(self):
        array = [
            "without_beard",
            "shaving",
            "flush_beard",
            "goatee_beard",
            "short_beard",
            "long_beard",
            "castaway_beard",
            "monk_beard"
        ]
        self.INNER = Basic().convertArrayToMap(array)
