



from data_model.core.battle.core.army.Army import Army
import random

class Battle:

    OBJECTIVES_IN_BATTLE_ARRAY = [
        "fallo arriba",
        "fallo derecha",
        "fallo izquierda",
        "fallo abajo",
        "face", #no estan protegidos
        "cabeza",
        "cuello", #no estan protegidos
        "brazos",
        "pecho",
        "panza",
        "cintura", #no estan protegidos
        "cadera",
        "piernas"
    ]

    def __init__(self):
        self.whoStart = 1
        self.combatIsEnd = False
        self.resultCombat = "el ganador es"
        self.textCombat = ""
        self.winnerCode = 0
        self.army1 = Army()
        self.army2 = Army()
        return

    def writeBattleStage(self):
        text = ""
        text += self.army1.personArray[0].writePersonUpdate(0)
        text += " se enfrento con el guerrero "
        text += self.army2.personArray[0].writePersonUpdate(0)
        text += self.textCombat
        if(self.combatIsEnd):
            text += "el ganador es el ejercito n°" + str(self.winnerCode)
        return text

    def performCombatByTurn(self):
        if(self.whoStart == 1):
            personAttacker = self.army1.personArray[0]
            personDefender = self.army2.personArray[0]
        elif(self.whoStart == 2):
            personAttacker = self.army2.personArray[0]
            personDefender = self.army1.personArray[0]
        #Battle
        personAttacker.addDailyEvent("participo en una batalla como atacante ")
        personDefender.addDailyEvent("participo en una batalla como defensor ")
        personAttacker.castAttack()
        personDefender.receiveAttack("", 1)
        #
        if(self.whoStart == 1):
            self.army1.personArray[0] = personAttacker
            self.army2.personArray[0] = personDefender
        elif(self.whoStart == 2):
            self.army2.personArray[0] = personAttacker
            self.army1.personArray[0] = personDefender

    def advanceOneDay(self,  date, visionData, auditionData, olfactoryData):
        if(self.combatIsEnd):
            return
        self.army1.advanceOneDay(date, visionData, auditionData, olfactoryData)
        self.army2.advanceOneDay(date, visionData, auditionData, olfactoryData)
        self.performCombatByTurn()
        if(not self.army1.thereAreSurvivors()):
            self.combatIsEnd = True
        if(not self.army2.thereAreSurvivors()):
            self.combatIsEnd = True
        return
