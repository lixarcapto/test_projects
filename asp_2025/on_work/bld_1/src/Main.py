


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
    actualMode = "region"
    marketTabKey = "vegetable"
    modesArray = ["market", "world", "region", "person", "build"]
    textToShow = ""
    basic = Basic()
    text = ""
    while(True):
        #print information--------------------------------------------
        textToShow = ""
        textToShow += "happyPeople = " + str(controller.dataModel.calculeHappyPeople())
        if(controller.dataModel.calculeHappyPeople() < 0):
            textToShow += " you lost "
        if(actualMode == "market"):
            iconListArray = controller.dataModel.writeMarketValues(marketTabKey)
            controller.view.paintMarketPopup(iconListArray)
        elif(actualMode == "world"):
            text = controller.dataModel.writeWorldMap()
            controller.view.printText(text)
        elif(actualMode == "person"):
            text = controller.dataModel.writePersonData()
            controller.view.printText(text)
        elif(actualMode == "nation"):
            text = controller.dataModel.writeNationData()
            controller.view.printText(text)
        elif(actualMode == "force"):
            text = controller.dataModel.writeArmyData()
            controller.view.printText(text)
        elif(actualMode == "build"):
            text = controller.dataModel.writeBuildInformation()
            controller.view.printText(text)
        elif(actualMode == "region"):
            text = controller.dataModel.writeMap()
            controller.view.paintRegionMap(text)
        controller.view.printText(controller.dataModel.obtainMessagesOnHold())
        controller.view.printText(textToShow)
        #----------------------------------------------------------------
        userInput = input()
        #input management-----------------------------------------------------
        if(userInput == "end"):
            break
        elif(userInput.find("build ") != -1):
            symbol = basic.extractFromString(userInput, "build ", " ")
            y = basic.extractFromString(userInput, "in ", " ")
            x = basic.extractFromString(userInput, "with ", " ")
            recipe = basic.extractFromString(userInput, "todo ", "*//")
            controller.dataModel.build(symbol, int(y), int(x), recipe)
        if(userInput == "a"):
            controller.dataModel.advanceTime()
        elif(userInput.find("market ") != -1):
            actualMode = "market"
            marketTabKey = basic.extractFromString(userInput, "market ", "*//")
        elif(userInput == "w"):
            actualMode = "world"
        elif(userInput == "n"):
            actualMode = "nation"
        elif(userInput == "r"):
            actualMode = "region"
        elif(userInput == "p"):
            actualMode = "person"
        elif(userInput == "f"):
            actualMode = "force"
        elif(userInput.find("goto ") != -1):
            regionCode = basic.extractFromString(userInput, "goto ", " ")
            districtCode = basic.extractFromString(userInput, "in ", "*//")
            if(regionCode == ""):
                regionCode = 0
            controller.dataModel.actualRegionSelected = int(regionCode)
            controller.dataModel.actualDistrictSelected = int(districtCode)
        elif(userInput.find("recruit ") != -1):
            personCode = basic.extractFromString(userInput, "recruit ", "*//")
            controller.dataModel.recruitPersonInRegionByCode(int(personCode))
        elif(userInput == "b"):
            actualMode = "build"
        controller.dataModel.world.messagesOnHold += basic.obtainMessagesOnHold()
        #-----------------------------------------------------------------
        system("cls")

main()
