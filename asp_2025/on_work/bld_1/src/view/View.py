

from os import system

from view.StorytellerPopup import StorytellerPopup
from basic.Basic import Basic

class View:

    def __init__(self):
        self.imagePopup = None
        self.sizeImageRegion = 70
        return

    def clear(self):
        system("cls")

    def printText(self, text):
        print(text)

    def catchText(self):
        return input()

    def paintRegionMap(self, namesImageStringMatrix):
        imagePopup = Basic().graphic().imagePopup()
        self.imagePopup = imagePopup.drawImageNamesMatrix(namesImageStringMatrix,
        [70, 70])

    def paintMarketPopup(self, iconListArray):
        imagePopup = Basic().graphic().imagePopup()
        paintOrder = imagePopup.createPaintOrder()
        paintOrder.addIconListArrayAsImages(iconListArray, [70, 70],
        [30, 0], 8, 150)
        imagePopup.setPaintOrder(paintOrder)
        imagePopup.drawImage()
