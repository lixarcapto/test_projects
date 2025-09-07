

from data_model.DataModel import DataModel
from data_model.core.region.Region import Region
from data_model.core.market.Market import Market
from data_model.core.world.World import World

def main():
    world = World()
    world.createNewWorld(40, 50)
    userInput = ""
    printType = ""
    while(True):
        world.advanceOneDay()
        userInput = input()
        if(userInput == "m"
        or userInput == "s"
        or userInput == "r"):
            printType = userInput
        if(userInput == "c"):
            userInput = input("building")
            building = userInput
            userInput = input("recipe")
            recipe = userInput
            world.createBuilding(building, recipe)
        if(printType == "m"):
            print(world.writeMarketInformation())
        if(printType == "r"):
            print(world.writeRegionInformation())
        if(printType == "s"):
            print(world.writeSocietyInformation())
    """
    userInput = ""
    dataModel = DataModel()
    dataModel.createNewScenario()
    while(True):
        dataModel.advanceOneDay()
        userInput = input()
        text = dataModel.writeCitizenInformation()
        print(text)
    """

main()
