



class Person:

    def __init__(self):
        #data personal
        self.codeInt = 0
        self.name = ""
        self.secondName = ""
        self.lastName = ""
        self.secondLastName = ""
        self.nickName = ""
        self.profession = 0
        self.mood = 0
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
        return

    def calculeMood(self):
        if(self.hasHome):
            self.mood += 1
        if(self.hasFood):
            self.mood += 1
        if(self.hasWater):
            self.mood += 1
        if(self.hasProtein):
            self.mood += 1
        if(self.hasVitamin):
            self.mood += 1
        if(self.hasFat):
            self.mood += 1
        if(self.hasSalt):
            self.mood += 1
        if(self.hasSpices):
            self.mood += 1
        if(self.hasFurnitures):
            self.mood += 1

    def consumeMarket(self, market):
        if(market.hasResource(market.MARKET_GLOBAL_KEYS["sweet-water-vessel"], 1)):
            market.consumeResource(market.MARKET_GLOBAL_KEYS["sweet-water-vessel"], 1)
            self.hasWater = True
        if(market.hasResource(market.MARKET_GLOBAL_KEYS["salt-bag"], 1)):
            market.consumeResource(market.MARKET_GLOBAL_KEYS["salt-bag"], 1)
            self.hasSalt = True
        return market

    def advanceTime(self, market):
        market = self.consumeMarket(market)
        self.calculeMood()
        return market

    def writeData(self):
        text = ""
        text += "code: " + str(self.codeInt) + "\n"
        text += "mood: " + str(self.mood) + "\n"
        text += "name: " + self.name + "\n"
        text += "secondName: " + self.secondName + "\n"
        text += "lastName: " + self.lastName + "\n"
        text += "secondLastName: " + self.secondLastName + "\n"
        return text
