
import os
from data_model.firm.messages.DesitionMessage import DesitionMessage
from presenter.link.RequestMessage import RequestMessage

class Presentation:

    def __init__(self):
        self.title = ""
        self.textInScreen = ""
        return

    def cleanScreen(self):
        os.system("cls")

    def setTitle(self, text):
        self.title = text

    def setText(self, text):
        self.textInScreen = text

    def printText(self):
        textLines = ""
        symbolLines = "--"
        textTitle = ""
        for i in range(10):
            textLines += symbolLines
        textTitle = textLines + textLines + textLines + textLines + "\n"
        textTitle += textLines + " " + self.title + " " + textLines + "\n"
        textTitle +=  textLines + textLines + textLines + textLines + "\n"
        print(textTitle)
        print(self.textInScreen + "\n")

    def update(self):
        self.cleanScreen()
        self.printText()

    def waitEnter(self):
        input()

    def requestOptions(self, text, optionsArray, separatorSymbol, distanceBetwenMargin):
        userInput = ""
        n = 0
        spaceText = ""
        for i in range(distanceBetwenMargin):
            spaceText += " "
        while(True):
            n = 0
            self.update()
            print(text + "\n")
            for e in optionsArray:
                print(spaceText + separatorSymbol + str(n) + " " + e)
                n += 1
            userInput = input()
            if(userInput == "0"
            or userInput == "1"
            or userInput == "2"
            or userInput == "3"
            or userInput == "4"
            or userInput == "5"
            or userInput == "6"
            or userInput == "7"
            or userInput == "8"
            or userInput == "9"):
                return userInput
            print("respuesta no valida.")
            self.waitEnter()

    def requestTextArray(self, requestMessage):
        question = None
        result = ""
        self.setText(requestMessage.updateText)
        for i in range(len(requestMessage.questionArray)):
            question = requestMessage.questionArray[i]
            result = self.requestOptions(question.text, question.optionsArray,
            requestMessage.separatorSymbol, requestMessage.distanceBetwenMargin)
            requestMessage.responseArray.append(result)
        return requestMessage

    def getText(self):
        return input()
