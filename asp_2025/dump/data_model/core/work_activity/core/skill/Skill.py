



from data_model.core.work_activity.core.AttackTypeMap import AttackTypeMap
from data_model.core.work_activity.core.DefenceTypeMap import DefenceTypeMap

class Skill:

    PERSON_WORK = None

    TYPE_EFFECT_KEYS = [
        "attack",
        "buff",
        "debuff"
    ]

    def __init__(self, personWork):
        Skill.PERSON_WORK = personWork
        self.requirementArea = [0] * 2
        self.effectsArray = []
        self.name = 0
        self.defianceName = 0
        return

    def createEffect(self, effectType, damageKey, value):
        array = [0] * 3
        array[0] = effectType
        array[1] = AttackTypeMap().INNER[damageKey]
        array[2] = value
        self.effectsArray.append(array)

    def createSkillCastLine(self):
        self.name = "cast_line",
        self.requirementArea[0] = Skill.PERSON_WORK[0]
        self.requirementArea[1] = 4
        self.createEffect("attack", "")
