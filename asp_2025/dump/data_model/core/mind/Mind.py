


from data_model.core.mind.app.task.RandomizeMentalTraitsTk import RandomizeMentalTraitsTk
from data_model.core.mind.app.task.CreateHistoryTk import CreateHistoryTk
from data_model.core.mind.app.task.WritePersonPresentationTk import WritePersonPresentationTk
from data_model.core.mind.app.task.WriteFullName import WriteFullName
from data_model.core.mind.app.task.TakeDesitionTk import TakeDesitionTk

from data_model.core.mind.app.product.MindProduct import MindProduct
from data_access.DataAccess import DataAccess
import random

class Mind:

    def __init__(self):
        self.inner = MindProduct()
        workMap = DataAccess().getMarketKeys().getWorkKeysMap()
        #practice matrix
        array = None
        self.inner._skillMatrix = [None] * (len(workMap))
        for i in range(len(self.inner._skillMatrix)):
            array = [None] * 2
            self.inner._skillMatrix[i] = array
            self.inner._skillMatrix[i][0] = i
            self.inner._skillMatrix[i][1] = 0

    def createSkillsMatrix(self):
        workMap = DataAccess().getMarketKeys().getWorkKeysMap()
        for i in range(len(self.inner._skillMatrix)):
            self.inner._skillMatrix[i][1] = random.randint(0, MindProduct.LIMIT_PRACTICE)
        self.inner._skillFavoritArray = [] * 2
        for i in range(len(self.inner._skillFavoritArray)):
            self.inner._skillFavoritArray[i] = random.randint(0,
            len(workMap) -1)
        self.inner._skillDisgustArray = [] * 2
        for i in range(len(self.inner._skillDisgustArray)):
            self.inner._skillDisgustArray[i] = random.randint(0,
            len(workMap) -1)
        self.inner._profession = random.randint(0, len(workMap) -1)

    def randomizeMentalTraits(self, culture, gender):
        randomizeMentalTraits = RandomizeMentalTraitsTk()
        self.createSkillsMatrix()
        self.inner = randomizeMentalTraits.inner(self.inner, culture, gender)

    def createHistory(self):
        createHistory = CreateHistoryTk()
        self.inner = createHistory.inner(self.inner)

    def writeFullName(self):
        writeFullName = WriteFullName()
        return writeFullName.inner(self.inner)

    def writePsychologicDescription(self):
        translator = Translator()
        text = ""
        return text

    def writeSensations(self):
        text = "sentia "
        translator = DataAccess().createTranslator()
        if(len(self.inner.sensationsDataArray) > 0):
            for i in range(len(self.inner.sensationsDataArray)):
                array = self.inner.sensationsDataArray[i]
                text += translator.obtainSensationsType(array[0]) + " en "
                text += translator.obtainOrganType(array[1]) + ", "
        else:
            text += "nada"
        return text

    def takeDesition(self):
        takeDesition = TakeDesitionTk()
        self.inner = takeDesition.inner(self.inner)

    def addDailyEvent(self, type, data, text):
        eventArray = [0] * 3
        eventArray[0] = type
        eventArray[1] = data
        eventArray[2] = text
        self.inner.dailyEventList.append(eventArray)

    def addSensation(self, type, cause):
        array = [None] * 2
        array[0] = type
        array[1] = cause
        self.inner.sensationsDataArray.append(array)

    def clearMemory(self):
        self.inner.sensationsDataArray.clear()

    def advanceOneDay(self):
        None
