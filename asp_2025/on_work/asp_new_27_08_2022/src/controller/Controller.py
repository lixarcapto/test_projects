

import os
from application.Application import Application

class Controller:

    def __init__(self):
        self.application = Application()
        self.application.initNewGame()
        self.mainLoop()
        return

    def listenEvents(self):
        if(self.application.protagonistIsDead()):
            self.application.addEvent("protagonist_is_dead", "")

    def reactToEvents(self):
        for e in self.application.eventQueueArray:
            if(e[0] == "protagonistIsDead"):
                None
            elif(e[0] == "user_input"):
                if(e[1] == "end"):
                    self.application.programIsOn = False
                elif(e[1] == "0"
                or e[1] == "1"
                or e[1] == "2"
                or e[1] == "3"
                or e[1] == "4"
                or e[1] == "5"
                or e[1] == "6"
                or e[1] == "7"
                or e[1] == "8"):
                    self.application.dataModel.takeDesitionWithProtagonist(int(userInput))
            elif(e[0] == "question_box_go_to_the_next_chapter"):
                if(e[1] == "yes"):
                    self.application.initNewLife()
                elif(e[1] == "no"):
                    self.application.programIsOn = False
            elif(e[0] == ""):
                None
            elif(e[0] == ""):
                None
            elif(e[0] == ""):
                None
            elif(e[0] == ""):
                None
            elif(e[0] == ""):
                None
            elif(e[0] == ""):
                None
            elif(e[0] == ""):
                None
            elif(e[0] == ""):
                None

    def mainLoop(self):
        userInput = ""
        while(self.application.programIsOn):
            self.listenEvents()
            self.reactToEvents()
            self.application.advanceOneDay()
            self.application.requestDesitionMessage()
            self.application.analyzeModelEvents()
        return
