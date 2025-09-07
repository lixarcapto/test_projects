



from data_model.core.sensory_description.core.sensory_data.SensoryData import SensoryData
from data_access.DataAccess import DataAccess

class Thing:

    """
        Añadir un secto sentido de movimiento, para describir cuando
        las cosas realizan alguna accion apreciable. Tambien añadir olor/sabor
        como un solo sentido.
    """

    def __init__(self):
        self.thingName = ""
        self.thingType = ""
        self.sensationsDataArray = []
        self.soundDataArray = []
        self.imageDataArray = []

    def define(self, name, type):
        self.thingName = name
        self.thingType = type

    def addExternalSensation(self, type, power):
        sensationMap = DataAccess().getMindKeysMap().getExternalSensationsKeysMap()
        array = [None] * 2
        array[0] = sensationMap[type]
        array[1] = power
        self.sensationsDataArray.append(array)

    def addSound(self, type, power):
        array = [None] * 2
        array[0] = type
        array[1] = power
        self.soundDataArray.append(array)

    #el origen indica a quien pertecen las imagenes, region por ejemplo
    def addImage(self, type, power):
        imageMap = DataAccess().getMindKeysMap().getImageKeysMap()
        array = [None] * 2
        array[0] = imageMap[type]
        array[1] = power
        self.imageDataArray.append(array)

    def writeSounds(self):
        return "se escuchaba como "

    def writeImages(self):
        text = "parecia "
        translator = DataAccess().createTranslator()
        array = None
        for i in range(len(self.imageDataArray)):
            array = self.imageDataArray[i]
            text += translator.obtainImageType(array[0]) + " "
            text += str(array[1]) + ", "
        return text

    def writeSensations(self):
        text = "se sentia "
        translator = DataAccess().createTranslator()
        array = None
        for i in range(len(self.sensationsDataArray)):
            array = self.sensationsDataArray[i]
            text += translator.obtainExternalSensationsType(array[0])
        return text

    def writeSmells(self):
        return ""

    def writeThing(self):
        text = ""
        text += self.thingName + " "
        text += self.thingType + " "
        text += self.writeImages() + ". \n"
        text += self.writeSounds() + ". \n "
        text += self.writeSensations() + ". \n"
        return text
