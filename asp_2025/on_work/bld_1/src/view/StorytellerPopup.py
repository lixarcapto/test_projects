

from basic.core.image_popup.ImagePopup2 import ImagePopup2
from view.StoryDate import StoryDate
from tkinter import *

class StorytellerPopup(ImagePopup2):

    def __init__(self):
        super().__init__()
        """
        self.text = Text(self.root, background = "yellow")
        self.text.place(width="500", height="200", x = "10", y = "400")
        """

        #tested--------------------------------------
        story1 = StoryDate()
        directionImages = "/Users/luisd/OneDrive/Escritorio/"
        directionImages += "py_proyects/bld_1/res/image/"
        imageOrder = story1.paintOrder.imageOrder([0, 0])
        imageOrder.addLayoutImage(directionImages + "paper_background.png", "image")
        imageOrder = story1.paintOrder.addImage(imageOrder)
        imageOrder = story1.paintOrder.imageOrder([0, 0])
        imageOrder.addLayoutImage(directionImages + "tent.png", "image")
        imageOrder = story1.paintOrder.addImage(imageOrder)
        imageOrder = story1.paintOrder.imageOrder([20, 0])
        imageOrder.addLayoutImage(directionImages + "fish_product.png", "image")
        story1.paintOrder.addSerieImage(imageOrder, 20, "x", 4)
        imageOrder = story1.paintOrder.imageOrder([300, 400])
        imageOrder.addLayoutImage(directionImages + "caviar.png", "image")
        story1.paintOrder.addSerieImage(imageOrder, 60, "y", 4)
        imageOrder = story1.paintOrder.imageOrder([400, 0])
        imageOrder.addLayoutImage("la comida va aqui", "text")
        story1.paintOrder.addImage(imageOrder)
        iconListArray = []
        array = None
        for i in range(5):
            array = []
            array.append(directionImages + "region/market_icon/bones.png")
            array.append(" \n          = 0")
            iconListArray.append(array)
        story1.paintOrder.addIconListArrayAsImages(iconListArray,
        [50, 50], [0, 0])
        #-------------------------------------
        self.drawStory(story1)
        return

    def drawStory(self, storyDate):
        self.setPaintOrder(storyDate.paintOrder)
        #
        #self.text.delete(1.0,"end")
        #self.text.insert(1.0, storyDate.text)
        self.drawImage()
        return
