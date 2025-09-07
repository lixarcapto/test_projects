



import os

class Presenter:

    def __init__(self):
        return

    def clean(self):
        os.system("cls")

    def receiveText(self, text):
        print(text)

    def requestText(self):
        return input()

    def initMainScreen(self):
        print("proyect")

    def initGameScreen(self):
        print("gameScreen")

    def sortText(self, text, sizeLine):
        charact = ""
        newText = ""
        countSizeLine = 0
        for i in range(len(text)):
            charact = text[i:i +1]
            countSizeLine += 1
            newText += charact
            if(charact == "\n"):
                countSizeLine = 0
            if(charact == " " and countSizeLine >= sizeLine):
                countSizeLine = 0
                newText += "\n"
        return newText

    def addMarginText(self, text, marginSize):
        charact = ""
        newText = ""
        space = ""
        for i in range(marginSize):
            space += " "
        for i in range(len(text)):
            charact = text[i:i +1]
            newText += charact
            if(charact == "\n"):
                newText += space
        return newText

    def receiveQuestMessage(self, message):
        sizeLine = 100
        marginSize = 10
        self.clean()
        text = ""
        text += "---" + message.title + "---\n"
        text += message.text
        text += message.quest
        n = 0
        for e in message.optionsArray:
            text += "\n " + str(n) + "> " + e
            n += 1
        text = self.sortText(text, sizeLine)
        text = self.addMarginText(text, marginSize)
        print(text)

    def receiveTextSecuenceMessage(self, message):
        self.clean()
        print("---" + message.title + "---\n")
        for e in message.textArray:
            self.clean()
            print("\n\n\n\n\n\n\n\n\n\n\n")
            print("         " + e)
            input("         " + message.skipText)
