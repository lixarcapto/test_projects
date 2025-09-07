


from controller.Controller import Controller
from os import system
import random
from basic.Basic import Basic

def main():
    print("init")
    controller = Controller()
    controller.dataModel.createNewMap()
    userInput = ""
    messagesOnHold = ""
    basic = Basic()
    while(True):
        userInput = input()
        system("cls")
        if(userInput == "f"
        or userInput == "end"):
            break
        elif(userInput.find("build ") != -1):
            symbol = basic.extractFromString(userInput, "build ", " ")
            y = basic.extractFromString(userInput, "in ", " ")
            x = basic.extractFromString(userInput, "with ", " ")
            recipe = basic.extractFromString(userInput, "todo ", ".")
            print(symbol + " " + y + " " + x + " " + recipe)
            controller.dataModel.build(symbol, int(y), int(x), recipe)
        if(userInput == "a"):
            controller.dataModel.advanceTime()
            print(controller.dataModel.writeMap())
        elif(userInput == "m"):
            print(controller.dataModel.writeMarketValues())
        elif(userInput == "p"):
            print(controller.dataModel.writePersonData())
        elif(userInput.find("goto ") != -1):
            regionCode = basic.extractFromString(userInput, "goto ", ".")
            if(regionCode == ""):
                regionCode = 0
            controller.dataModel.actualRegionSelected = int(regionCode)
            print(controller.dataModel.writeMap())
        elif(userInput == "b"):
            print(controller.dataModel.writeBuildInformation())
        else:
            print(controller.dataModel.writeMap())
        controller.dataModel.world.messagesOnHold += basic.obtainMessagesOnHold()
        print(controller.dataModel.obtainMessagesOnHold())

main()
