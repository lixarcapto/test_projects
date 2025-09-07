


from data_model.DataModel import DataModel
from presenter.Presenter import Presenter

class Application:

    def __init__(self):
        self.programIsOn = True
        self.dataModel = DataModel()
        self.presenter = Presenter()

    def initProgram(self):
        self.initMainScreen()

#*** MAIN SCREEN ************************************************************************

    def updateMainScreen(self):
        message = self.dataModel.requestMainScreenMessage()
        self.presenter.receiveQuestMessage(message)

    def initMainScreen(self):
        self.presenter.initMainScreen()
        self.updateMainScreen()
        response = self.presenter.requestText()
        self.analyseResponseMainScreen(response)

    def initNewGame(self):
        self.dataModel.createNewScenario()
        self.dataModel.initNewLife()

    def advanceOneDay(self):
        self.dataModel.advanceOneDay()

    def analyseResponseMainScreen(self, data):
        if(data == "0"):
            self.initIntroScreen()
        elif(data == "1"):
            None
        elif(data == "2"):
            None
        elif(data == "3"):
            None
        elif(data == "4"):
            None
        elif(data == "5"):
            None

#*** GAME SCREEN ***************************************************************************

    def analyseResponseDesitionMessage(self, data):
        if(data == "0"):
            None
        elif(data == "1"):
            None
        elif(data == "2"):
            None
        elif(data == "3"):
            None
        elif(data == "4"):
            None
        elif(data == "5"):
            None

    def initGameScreen(self):
        self.initNewGame()
        while(True):
            message = self.dataModel.requestDesitionMessage()
            self.presenter.receiveQuestMessage(message)
            response = self.presenter.requestText()
            if(response == ""):
                response = "0"
            if(response == "f" or response == "end"):
                break
            self.dataModel.receiveDesitionResponse(response)
            message = self.dataModel.requestDesitionMessageDataAccordingToDesition(response)
            self.presenter.receiveQuestMessage(message)
            response = self.presenter.requestText()
            self.advanceOneDay()

#--- intro --------------------------------------------------------------------------

    def initIntroScreen(self):
        message = self.dataModel.requestIntroMessage()
        self.presenter.receiveTextSecuenceMessage(message)
        self.initGameScreen()
