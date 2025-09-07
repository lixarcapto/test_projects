




from basic.Basic import Basic

class TopicKeysMapData:

    def __init__(self):
        array = [
            #negative
            "pain",
            "nauseas",
            "cold",
            "heat",
            "paralysis",
            "irritation",
            "tickle",
            "fatigue",
            "dryness",
            "tremors",
            "",
            "",
            "",
            "",
            "",
            "",
            #neuter
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            #positive
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        self.INNER = Basic().convertArrayToMap(array)
        return
