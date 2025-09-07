



from data_access.DataAccess import DataAccess

class Skill:

    STAT_TYPE = [
        "",
        "",
        ""
    ]

    EFFECT_TYPE = [
        "buff",
        "debuff",
        "attack"
    ]

    def __init__(self):
        self.name = ""
        self.effectType = 0
        self.statType = 0
        self.statModifier = 0
        return
