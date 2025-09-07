



from data_access.DataAccess import DataAccess

class Memory:

    LEVEL_SENSATION_TEXT_ARRAY = [ #0 a 5
        "lijero",
        "leve",
        "medio",
        "regular",
        "notable",
        "fuerte"
    ]

    IMAGE_TYPE_TEXT_ARRAY = [ #0 a 5
        "lijero",
        "leve",
        "medio",
        "regular",
        "notable",
        "fuerte"
    ]

    IMAGE_ORIGEN_KEYS_ARRAY = [ #0 a 5
        "region",
        "person",
        "animal",
        "unknown"
    ]

    def __init__(self):
        self.sensationsDataArray = []
        self.soundDataArray = []
        self.imageDataArray = []
        self.actualDate = None
        return

    def addSensation(self, type, origen, power):
        sensationMap = DataAccess().getMindKeysMap().getSensationKeysMap()
        organMap = DataAccess().getPersonKeys().getOrganTypeMap()
        array = [None] * 3
        array[0] = sensationMap[type]
        array[1] = organMap[origen]
        array[2] = power
        self.sensationsDataArray.append(array)

    def addSound(self, type, origen, power):
        array = [None] * 3
        array[0] = type
        array[1] = origen
        array[2] = power
        self.soundDataArray.append(array)

    #el origen indica a quien pertecen las imagenes, region por ejemplo
    def addImage(self, type, origen, power):
        imageMap = DataAccess().getMindKeysMap().getImageKeysMap()
        array = [None] * 3
        array[0] = imageMap[type]
        array[1] = origen
        array[2] = power
        self.imageDataArray.append(array)

    def addEvent(self, type, origen, power):
        array = [None] * 3
        array[0] = type
        array[1] = origen
        array[2] = power
        self.eventDataArray.append(array)

    def writeEvents(self):
        return ""

    def writeSounds(self):
        return "se escuchaba "

    def writeImages(self):
        text = "podia ver "
        translator = DataAccess().createTranslator()
        array = None
        for i in range(len(self.imageDataArray)):
            array = self.imageDataArray[i]
            text += translator.obtainImageType(array[0]) + " "
            text += array[1] + " en "
            text += str(array[2]) + ", "
        return text

    def writeSensations(self):
        text = "sentia "
        translator = DataAccess().createTranslator()
        array = None
        for i in range(len(self.sensationsDataArray)):
            array = self.sensationsDataArray[i]
            text += "un " +  Memory.LEVEL_SENSATION_TEXT_ARRAY[array[0]] + " "
            text += translator.obtainSensationsType(array[0]) + " en "
            text += translator.obtainOrganType(array[1]) + ", "
        return text

    def writeMemory(self):
        text = ""
        text += self.writeImages() + ". \n"
        text += self.writeSounds() + ". \n "
        text += self.writeSensations() + ". \n"
        return text
