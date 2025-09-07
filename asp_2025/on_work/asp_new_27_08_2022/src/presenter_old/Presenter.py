



from presenter.core.presentation_lib.Presentation import Presentation

class Presenter:

    def __init__(self):
        self.actualScreen = "none"
        self.mainScreen = None
        self.initMainScreen()
        return

    def initMainScreen(self):
        self.mainScreen = Presentation()
        self.mainScreen.setTitle("ASP proyect")

    def sendQuestionMessage(self, requestMessage):
        return self.mainScreen.requestTextArray(requestMessage)
