


from data_model.app.mind_lib.app.task.RandomizeMentalTraitsTk import RandomizeMentalTraitsTk
from data_model.app.mind_lib.app.task.CreateHistoryTk import CreateHistoryTk
from data_model.app.mind_lib.app.task.WritePersonPresentationTk import WritePersonPresentationTk
from data_model.app.mind_lib.app.task.WriteFullName import WriteFullName
from data_model.app.mind_lib.app.task.TakeDesitionTk import TakeDesitionTk

from data_model.app.mind_lib.app.product.MindProduct import MindProduct

from data_model.app.translator_lib.Translator import Translator

class Mind:

    def __init__(self):
        self.inner = MindProduct()

    def randomizeMentalTraits(self, culture, gender):
        randomizeMentalTraits = RandomizeMentalTraitsTk()
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

    def takeDesition(self):
        takeDesition = TakeDesitionTk()
        self.inner = takeDesition.inner(self.inner)

    def addDailyEvent(self, type, data, text):
        eventArray = [0] * 3
        eventArray[0] = type
        eventArray[1] = data
        eventArray[2] = text
        self.inner.dailyEventList.append(eventArray)
