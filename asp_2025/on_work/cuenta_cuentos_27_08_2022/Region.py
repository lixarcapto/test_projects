
import Person as Person

class Region:

    limitPersonInt = 50
    reliefNamesArray = ["inalcansable cima", "escarpada", "llana", "baja", "revoltosa agua",
    "profunda agua"]
    biomeNamesArray = ["el desierto", "el oceano", "la playa", "la montaña",
    "el pico", "el volcan"]

    def __init__(self):
        self.personArray = [None] * Region.limitPersonInt
        self.name = "athos"
        self.code = 0
        self.coordinateX = 0
        self.coordinateY = 0
        self.biomeType = 0
        self.soilType = 0
        self.relief = 0
        self.temperature = 0
        self.windSpeed = 0
        self.zoneLocation = 0
        self.climeType = 0
        self.temperatureRegime = 0
        self.windRegime = 0

    def setCoordianteX(self, value):
        self.coordinateX = value

    def setCoordianteY(self, value):
        self.coordinateY = value

    def setCode(self, value):
        self.code = value

    def writeRegionData(self):
        textStr = ""
        textStr += " en la " + self.reliefNamesArray[self.relief] + " de "
        textStr += self.biomeNamesArray[self.biomeType] + " " + self.name + "  "
        return textStr

    def advanceTime(self):
        for i in range(Region.limitPersonInt):
            if(self.personArray[i] == None):
                continue
            self.personArray[i].advanceTime(self.temperature)
        return None

    def addPerson(self, person):
        for i in range(Region.limitPersonInt):
            if(self.personArray[i] != None):
                continue
            self.personArray[i] = person
        return None

    def deletePerson(self, code):
        for i in range(limitPersonInt):
            if(self.personArray[i] == None):
                continue
            if(self.personArray[i].code == code):
                self.personArray[i].destroy()
                self.personArray[i] = None

    def getPerson(self, code):
        for i in range(Region.limitPersonInt):
            if(self.personArray[i] == None):
                continue
            if(self.personArray[i].code == code):
                return self.personArray[i]
