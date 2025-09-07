





from basic.Basic import Basic

class AttackTypeMap():

    def __init__(self):
        array = [
            "strenght",
            "intelligence",
            "magic",
            "cutting",
            "penetrating",
            "talisman",
            "courage",
            "intimidation",
            "push",
            "bullet",
            "fire",
            "real"
        ]
        self.INNER = Basic().convertArrayToMap(array)
