

from data_access.DataAccess import DataAccess
from data_model.core.product_list.ProductList import ProductList
from basic.Basic import Basic
import random

class Person:

    HEALTHY_BASIC_LEVEL = 5
    REMAINING_SATISFIED_TIME = 5

    def __init__(self):
        #STATES -----------------------------------------------------------------
        self.isDead = False
        #---------------------------------------------------------------------
        #data personal
        self.codeInt = 0
        self.name = ""
        self.secondName = ""
        self.lastName = ""
        self.secondLastName = ""
        self.nickName = ""
        self.profession = 0
        self.mood = 0
        self.needArray = []
        self.cultureCode = 0

        #EQUIPMENT----------------------------------------------------------

        self.weapon = None
        self.armor = None
        self.mount = None

        # PERSONAL VALUES ---------------------------------------------------

        self.energy = 0
        self.magicEnergy = 0
        self.bloodLost = 0
        self.temperature = 0
        self.loyalty = 0
        self.stress = 0
        self.toxicInVeinsLevel = 0
        self.pain = 0
        self.dirt = 0
        self.concentration = 0
        self.openWoundLevel = 0
        self.infectionLevel = 0
        self.accumulatedWaste = 0

        #SISTEMAS CORPORALES---------------------------------------------------
        array = [
            "audition",
            "smell",
            "vision",
            "legs",
            "arms",
            "respiratorySystem",
            "circulatorySystem",
            "inmuneSystem",
            "reproductiveSystem",
            "digestiveSystem",
            "filterSystem",
            "lowDigestiveSystem",
            "skin",
            "musculature",
            "oralHealth",
            "brainHealth",
            "column"
        ]
        self.systemsMap = Basic().convertStringArrayToMapNumber(array,
        Person.HEALTHY_BASIC_LEVEL)

        #COMBAT VALUES-------------------------------------------

        array = [
            #COMBAT VALUES --------------------------------------------
            "stinging",
            "shield",
            "cutting",
            "armor",
            "dent",
            "agility",
            "push",
            "blow",
            "magical",
            "talisman",
            "hex",
            "divine-luck",
            "bullet",
            "bulletproof",
            "laser",
            "mirror",
            "fire",
            "insulating",
            "electric",
            "piercing",
            "turret",
            "cold",
            "toxic",
            "mask",
            "radiation",
            "anti-radiation",
            "burst",
            "heavy-armor",
            "infection",
            "intimidating",
            "courage",
            "confusion",
            "intelligence",
            "bribery",
            "attractive"

        ]
        self.attackValuesMap = Basic().convertStringArrayToMapNumber(array, 0)

        #-------------------------------------------------------------

        #---------------------------------------------------------------------


        #---------------------------------------------------------------------
        #needs
        self.hasHome = False
        self.hasFood = False
        self.hasWater = False
        self.hasProtein = False
        self.hasVitamin = False
        self.hasFat = False
        self.hasSalt = False
        self.hasSpices = False
        self.hasFurnitures = False
        self.addBasicNeeds()
        return

    def productList(self):
        return ProductList()

    def addNeed(self, name, productList):
        map = dict()
        map["name"] = name
        map["productArray"] = productList
        map["remainingSatisfiedTime"] = 10
        map["isItSatisfied"] = True
        self.needArray.append(map)

    def addBasicNeeds(self):
        productList = self.productList()
        productList.addProduct("global", "water", 1)
        self.addNeed("water", productList)
        productList = self.productList()
        productList.addProduct("global", "chicken_meat", 1)
        productList.addProduct("global", "cow_meat", 1)
        productList.addProduct("global", "pig_meat", 1)
        self.addNeed("meat", productList)

    def calculeMood(self):
        self.mood = 0
        for i in range(len(self.needArray)):
            if(self.needArray[i]["isItSatisfied"]):
                self.mood += 1
            else:
                self.mood -= 1

    def consumeMarket(self, market):
        productValue = None
        map = None
        for i in range(len(self.needArray)):
            map = self.needArray[i]
            for t in range(len(map["productArray"].productArray)):
                productValue = map["productArray"].productArray[t]
                if(market.hasResource(productValue[1], productValue[2])):
                    market.consumeResource(productValue[1], productValue[2])
                    map["isItSatisfied"] = True
                    map["remainingSatisfiedTime"] = 10
                    map["productArray"].productArray[t] = productValue
                    break
            if(map["remainingSatisfiedTime"] >= 1):
                map["remainingSatisfiedTime"] -= 1
            if(map["remainingSatisfiedTime"] == 0):
                map["isItSatisfied"] = False
            self.needArray[i] = map
        return market

    def advanceTime(self, market):
        market = self.consumeMarket(market)
        self.calculeMood()
        self.performsMetabolism()
        return market

    def writeIndicatorsWithMaximumLimitAsBars(self):
        map = dict()
        map["blood-lost"] = self.bloodLost
        map["stress"] = self.stress
        map["toxic"] = self.toxicInVeinsLevel
        map["pain"] = self.pain
        map["dirt"] = self.dirt
        map["open-wound-level"] = self.openWoundLevel
        map["infection-level"] = self.infectionLevel
        return Basic().convertNumberMapToArrayStringBars(map, 1, 5, 10, ">")

    def writeIndicatorsWithMinimumLimitAsBars(self):
        map = dict()
        map["energy"] = self.energy
        map["magic-energy"] = self.magicEnergy
        map["loyalty"] = self.loyalty
        map["concentration"] = self.concentration
        return Basic().convertNumberMapToArrayStringBars(map, 1, 5, 10, "<")

    def performsMetabolism(self):
        if(self.isDead):
            return
        LIMIT_BLOOD_LOST = 10
        #GENERAR VALORES--------------------------------------------

        #pierde sangre por heridas abiertas
        self.bloodLost += self.openWoundLevel
        #genera infecciones por heridas abiertas
        if(self.openWoundLevel):
            self.infectionLevel += 1
        #combate infecciones
        if(self.systemsMap["inmuneSystem"] > 0):
            if(self.infectionLevel > 1):
                self.infectionLevel -= 1
        #combate toxicos
        if(self.systemsMap["filterSystem"] > 0):
            if(self.toxicInVeinsLevel > 1):
                self.infectionLevel -= 1
        #DETECTAR MUERTE ----------------------------------------
        if(self.systemsMap["circulatorySystem"] == 0):
            self.die()
        if(self.systemsMap["respiratorySystem"] == 0):
            self.die()
        if(self.systemsMap["brainHealth"] == 0):
            self.die()
        #CAUSAR DAÑO POR INDICADORES-----------------------------------------
        if(self.bloodLost >= LIMIT_BLOOD_LOST):
            self.die()
        return

    def damageSystem(self, keySystem, quantity):
        if(self.systemsMap[keySystem] >= quantity):
            self.systemsMap[keySystem] -= quantity
        else:
            self.systemsMap[keySystem] == 0

    def die(self):
        self.isDead = True
        return

    def causeAleatoryDamage(self, quantity):
        number = Basic().randomIndex(len(self.systemsMap))
        print("key : " +str(number))
        key = Basic().obtainKey(self.systemsMap, number)
        self.damageSystem(key, quantity)

    def receiveAttack(self, quantity):
        self.causeAleatoryDamage(quantity)
        return

    def writeData(self):
        symbolBar = Basic().colorString("white", "green") + "|"
        symbolBar += Basic().colorString("white", "black")
        text = ""
        text += "code: " + str(self.codeInt) + "\n"
        text += "mood: " + str(self.mood) + "\n"
        text += "name: " + self.name + "\n"
        text += "secondName: " + self.secondName + "\n"
        text += "lastName: " + self.lastName + "\n"
        text += "secondLastName: " + self.secondLastName + "\n"
        text += "culture: " + self.secondLastName + "\n"
        text += "\n\n"
        matrix = []
        array = Basic().convertNumberMapToArrayStringBars(self.systemsMap,
        1, 3, 10, "<")
        matrix.append(array)
        array = self.writeIndicatorsWithMaximumLimitAsBars()
        matrix.append(array)
        array += self.writeIndicatorsWithMinimumLimitAsBars()
        matrix.append(array)
        text += Basic().writeStringMatrixAsColumns(matrix)
        text += "\n\n"

        return text
