





from basic.Basic import Basic

class DefenceTypeMap():

    def __init__(self):
        array = [
            "physical_resistance",
            "mental_toughness",
            "magic_defense",
            "armor",
            "shield",
            "talisman",
            "courage",
            "speed",
            "firmness",
            "antibullet",
            "insulating"
        ]
        self.INNER = Basic().convertArrayToMap(array)
