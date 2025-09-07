


from data_model.core.work_activity.core.skill.Skill import Skill
import random
from basic.Basic import Basic

class PersonWork:

    PERSON_WORK = None
    LIMIT_PRACTICE = 10
    DEFENSE_TYPE_ARRAY = [
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
    ATTACK_TYPE_ARRAY = [
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
        "fire"
    ]

    def __init__(self, workAreas):
        PersonWork.PERSON_WORK = workAreas
        self.practicesAreasArray = None
        self.favoriteAreasArray = [0] * 2
        self.disgustAreasArray = [0] * 2
        self.skillsArray = []
        #ataques
        self.strenght = 1
        self.intelligence = 1 #causa ataque de stress
        self.magic = 1
        self.courage = 1
        self.firm = 1
        #los demas ataques los aportan las armas y otros
        #defensas
        self.physicalResistance = 1 #anti golpes suaves fisicos y fuerzas
        self.mentalToughness = 1 #anti stress
        self.magicDefense= 1 #magia
        self.armor = 1 #anticortante
        self.shield = 1 #antipenetrante
        self.talisman = 1 #antiespiritualidad
        self.courage = 1 #anti intimidacion
        self.speed = 1 #anti aplastante
        self.antimagic = 1
        self.firmness = 1 #ANTI empujones(push)
        self.antibullet = 1
        self.insulating = 1 #contra quemaduras y venenos
        #
        self.energy = 10
        self.timeRemaining = 10
        return

    def randomizeSkills(self):
        
        return

    def randomize(self):
        for i in range(len(self.favoriteAreasArray)):
            self.favoriteAreasArray[i] = random.randint(0,
            len(PersonWork.PERSON_WORK) -1)
        for i in range(len(self.disgustAreasArray)):
            self.disgustAreasArray[i] = random.randint(0,
            len(PersonWork.PERSON_WORK) -1)
        #practice matrix
        array = None
        self.practicesAreasArray = [None] * len(PersonWork.PERSON_WORK)
        for i in range(len(self.practicesAreasArray)):
            array = [None] * 2
            self.practicesAreasArray[i] = array
            self.practicesAreasArray[i][0] = i
            self.practicesAreasArray[i][1] = random.randint(0,
            PersonWork.LIMIT_PRACTICE)

    def writePersonWork(self):
        text = " sus habilidades eran "
        for i in range(len(self.practicesAreasArray)):
            text += PersonWork.PERSON_WORK[self.practicesAreasArray[i][0]] + " "
            text += str(self.practicesAreasArray[i][1]) + ", "
        return text
