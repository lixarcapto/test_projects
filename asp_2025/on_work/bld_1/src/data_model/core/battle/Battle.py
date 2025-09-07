


import random
from data_model.core.army.Army import Army
from basic.Basic import Basic

class Battle:

    def __init__(self):
        self.armyGarrison = Army()
        self.armyInvader = None
        self.aIsAttacker = True
        return

    def advanceTime(self):
        if(self.armyInvader == None):
            return
        self.armyAttacker = None
        self.armyDefender = None
        if(self.aIsAttacker):
            self.armyAttacker = self.armyGarrison
            self.armyDefender = self.armyInvader
        else:
            self.armyAttacker = self.armyInvader
            self.armyDefender = self.armyGarrison
        listAttacker = self.armyAttacker.personList
        listDefender = self.armyDefender.personList
        #
        personAttacker = None
        personObjetive = None
        aleatoryObjetiveIndex = 0
        for i in range(len(listAttacker.personArray)):
            #obtiene atacante y defensor persona
            personAttacker = listAttacker.personArray[i]
            aleatoryObjetiveIndex = Basic().randomIndex(listAttacker.size())
            personObjetive = listDefender.personArray[aleatoryObjetiveIndex]
            #realiza el ataque
            personObjetive.receiveAttack(1)
            #regresa al atacante y defensor
            listDefender.personArray[aleatoryObjetiveIndex] = personObjetive
            listAttacker.personArray[i] = personAttacker
        #
        self.armyAttacker.personList = listAttacker
        self.armyDefender.personList = listDefender
        if(self.aIsAttacker):
            self.armyAttacker = self.armyGarrison
            self.armyDefender = self.armyInvader
        else:
            self.armyInvader = self.armyAttacker
            self.armyGarrison = self.armyDefender
        #cambia el turno
        if(self.aIsAttacker):
            self.aIsAttacker = False
        else:
            self.aIsAttacker = True

    def writeBattleSituacion(self):
        return text
