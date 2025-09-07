



from view.View import View
from data_model.DataModel import DataModel
import threading

class Application:

    def __init__(self):
        self.view = View()
        self.thread = None
        self.thread2 = None
        self.dataModel = DataModel()
        self.view.buton.configure(command = self.advanceTime)
        self.initProgram()
        self.view.initLoop()
        return

    def advanceTime(self):
        self.dataModel.advanceTime()

    def initProgram(self):
        self.dataModel.createNewGame()
        if(self.view.event != None):
            print("yes click")
        return
