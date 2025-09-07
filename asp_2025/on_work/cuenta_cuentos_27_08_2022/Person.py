
import Basic as Basic
import Food as Food
import random

class Person:

    ageNamesArray = ["bebe", "niño", "adolecente", "joven", "adulto", "adulto mayor",
    "anciano", "moribundo"]
    faceNamesArray = ["aciatica", "occidental", "africana", "arabe",
    "extraña", "india americana"]
    heightNamesArray = ["gigante", "alto", "de mediana altura", "pequeño", "enano"]
    weightNamesArray = ["desnutrido", "escualido", "delgado",
    "en forma", "gordo", "obeso", "morbido"]
    skinColorNamesArray = ["piel palida", "piel blanca", "piel rosa", "piel arena",
    "piel roja", "piel oliva", "piel almendra","piel marron", "piel negra",
    "piel gris"]
    healthStatesNamesArray = ["perdido", "grave", "dañado", "recuperandose", "sano"]
    moodNamesArray = ["desesperado", "estresado", "nervioso", "calmado",
    "animado", "inspirado", "extasiado"]
    pronoumsArray = ["el", "ella"]
    actionsNamesArray = ["eat", "drink", "walk", "run"]
    ageLimit = 8
    confortTemperatureMax = 22.0
    confortTemperatureMin = 18.0
    mortalLimitTemperatureMax = 120
    mortalLimitTemperatureMin = -30
    heatstrokeTemperature = 47
    hypothermiaTemperature = 4
    moodLimitMax = 28
    moodLimitMin = 0

    def __init__(self):
        self.notifyToWrite = ""
        self.age = 4
        self.code = 0
        self.name = "juan"
        self.inventoryCapacity = 15
        self.inventoryArray = [] * self.inventoryCapacity
        self.whatAreYouDoingStr = ""
        self.actionsToDoArray = []
        """states"""
        self.isDeath = False
        self.hasSickness = False
        """0: male, 1:female"""
        self.mood = 9
        self.days = 0
        self.months = 0
        self.years = 0
        self.gender = 0
        self.lastName = "perez"
        self.secondLastName = "scott"
        self.skinColor = 0
        self.monthAge = 0
        self.bornDay = 0
        self.bornMonth = 0
        self.bornYear = 0
        self.weight = 4
        self.height = 2
        self.faceType = 0
        """values"""
        self.nutrients = 0
        self.minerals = 0
        self.vitamins = 0
        self.proteins = 0
        self.fats = 0
        self.water = 0
        self.salt = 0
        self.sugars = 0
        self.energy = 0
        self.temperature = 20.0
        """ml de sangre"""
        self.blood = 250
        self.oxigen = 0
        self.capacityOfEat = 5
        self.foodConsumedArray = [None] * self.capacityOfEat
        """needs"""
        self.hasHeat = False
        self.hasChill = False
        self.haveNotify = False
        self.hasHungry = False
        self.hasThist = False
        self.hasFun = False
        self.difficultBreathing = False
        """sickness"""
        """viral"""
        self.hasPestilence = False
        self.hasH1N1 = False
        self.hasH1N2 = False
        self.hasH1N3 = False
        self.SARScov2 = False
        self.SARScov1 = False
        self.smallpox = False
        self.HIV = False
        """not contagious"""
        self.cancer = False
        self.anemia = False
        self.sclerosis = False
        self.alzheimers = False
        self.dementia = False
        self.schizophrenia = False
        self.diabetes = False
        self.heatstroke = False
        self.hypothermiaTemperature = False
        self.coma = False
        """health"""
        self.conscience = 4
        self.heart = 4
        self.respiratorySystem = 4
        self.digestiveSystem = 4
        self.circulatorySystem = 4
        self.reproductiveSystem = 4
        self.immuneSystem = 4
        self.limbicSystemAndBrain = 4
        self.column = 4
        self.arms = 4
        self.legs = 4

    def setCode(self, value):
        self.code = value

    def getCode(self):
        return self.code

    def sumMood(value):
        if(Person.moodLimitMax <= value + self.mood
        or Person.moodLimitMin >= value + self.mood):
            self.mood += value

    def eatFood(self, food):
        for i in range(self.capacityOfEat):
            if(self.foodConsumedArray[i] == none):
             self.foodConsumedArray[i] = food
             return
        return -1

    def notifyStates(self):
       textStr = ""
       if(not self.haveNotify):
           self.notifyToWrite  = ""
           return
       textStr += " entonces " + self.name + " sintio"
       if(self.difficultBreathing):
           textStr += " dificultad para respirar y dolor en el pecho"
       self.notifyToWrite = textStr

    def consumeFood(self):
       food = Food.Food()
       i = 0
       for e in self.foodConsumedArray:
           i += 1
           if(e == None):
               continue
           food = e
           self.nutrients += food.nutrients
           self.minerals += food.minerals
           self.vitamins += food.vitamins
           self.proteins += food.proteins
           self.fats += food.fats
           self.water += food.water
           self.salt += food.salt
           self.sugars += food.sugars
           self.foodConsumedArray[i] = None
       return

    def getNotify(self):
       return self.notifyToWrite

    def advanceAge(self):
        self.days += 1
        if(self.days == 4):
            self.months += 1
        if(self.months == 4):
            self.years += 1
        if(self.years == 5):
            self.age += 1
        if(self.age > 8):
            self.isDeath = True

    def causeDiseases(self):
        if(self.temperature >= Person.mortalLimitTemperatureMax):
            self.heatstroke = True
        if(self.temperature < Person.mortalLimitTemperatureMax
        and self.temperature > Person.heatstrokeTemperature):
            if(random.randint(0, 100) >= 30):
                self.heatstroke = True
        if(self.temperature > Person.mortalLimitTemperatureMin
        and self.temperature < Person.hypothermiaTemperature):
            if(random.randint(0, 100) >= 50):
                self.hypothermia = True
        if(self.temperature >= Person.mortalLimitTemperatureMin):
            self.hypothermia = True

    def calculeMood(self):
        self.mood = 0
        if(self.hasSickness):
            self.sumMood(-1)
        if(self.hasChill):
            self.sumMood(-1)
        if(self.hasHeat):
            self.sumMood(-1)
        if(self.hasThist):
            self.sumMood(-1)
        if(self.hasHungry):
            self.sumMood(-1)

    def defineMoodName(self):
        stringStr = ""
        if(self.mood >= 0
        or self.mood < 4):
            stringStr = "enloquecido"
        if(self.mood >= 4
        or self.mood < 8):
            stringStr = "desesperado"
        if(self.mood >= 8
        or self.mood < 12):
            stringStr = "estresado"
        if(self.mood >= 12
        or self.mood < 4 * 4):
            stringStr = "nervioso"
        if(self.mood >= 4 * 4
        or self.mood < 20):
            stringStr = "calmado"
        if(self.mood >= 20
        or self.mood < 24):
            stringStr = "animado"
        if(self.mood >= 24
        or self.mood < 28):
            stringStr = "inspirado"
        if(self.mood > 28):
            stringStr = "extasiado"
        return stringStr

    def createNeeds(self):
        if(self.temperature > Person.confortTemperatureMax):
            self.hasHeat
        if(self.temperature < Person.confortTemperatureMin):
            self.hasChill

    def takeADecision(self, decisionKey):
        return

    def writeWhatAreYouDoing(self):
        self.actionsToDoArray = []
        textStr = Person.pronoumsArray[self.gender]
        textStr += " estaba " + self.whatAreYouDoingStr + "\n"
        textStr += "> " + "haciendo nada" + "\n"
        self.actionsToDoArray.append("haciendo nada")
        if(self.hasThist):
            textStr += "> " + "bebiendo" + "\n"
            self.actionsToDoArray.append("bebiendo")
        if(self.hasHungry):
            textStr += "> " + "comiendo" + "\n"
            self.actionsToDoArray.append("comiendo")
        decisionKey = input()
        self.takeADecision(decisionKey)
        return textStr

    def realizeBiologicalActivity(self):
        return

    def writeNeedsList(self):
        textStr = ""
        if(self.hasSickness):
            textStr += " una enfermedad"
        if(self.hasChill):
            textStr += " frio"
        if(self.hasHeat):
            textStr += " calor"
        if(self.hasThist):
            textStr += " sed"
        if(self.hasHungry):
            textStr += " hambre"
        else:
            textStr += " nada"
        return textStr

    def writeUpdateInformation(self):
        textStr = ""
        textStr += self.name + " " + self.lastName + " se sentia "
        textStr += self.defineMoodName() + " por tener " + self.writeNeedsList()
        return textStr

    def writeInformation(self):
       textStr = ""
       genderStr = ""
       if(self.gender == 0):
           genderStr = " un hombre"
       else:
           genderStr = " una mujer"
       textStr += self.name + " " + self.lastName + " " + self.secondLastName
       textStr +=  " " + genderStr + " " + self.ageNamesArray[self.age]
       textStr += " de apariencia " + self.faceNamesArray[self.faceType]
       textStr += " con " + self.skinColorNamesArray[self.skinColor] + ","
       textStr += " " + self.weightNamesArray[self.weight]
       textStr += " y " + self.heightNamesArray[self.height]
       return textStr

    def advanceTime(self, temperature):
       self.temperature = temperature
       self.advanceAge()
       self.causeDiseases()
       self.createNeeds()
       self.consumeFood()
       self.notifyStates()
       self.calculeMood()
       return

    def addToInventory(self, product):
        for i in range(self.inventoryCapacity):
            if(self.inventoryArray[i] == None):
                self.inventoryArray[i] = product
                return 0
        return -1

    def destroy(self):
        return
