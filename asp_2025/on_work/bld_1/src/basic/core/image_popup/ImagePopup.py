

from tkinter import *

class ImagePopup:

    def __init__(self):
        sizeFrameX = "1300"
        sizeFrameY = "700"
        self.root = None
        self.root = Tk()
        self.root.pack_propagate(False)
        self.frame = Frame(self.root)
        self.frame.config(height = sizeFrameY, width = sizeFrameX, background = "black")
        self.frame.place(x = "0", y = "0")
        self.frame.pack_propagate(False)
        self.frame.grid_propagate(False)
        self.button = Button(self.frame, text='doit', command='doit')
        self.button.pack_propagate(False)
        self.button.place(x = "0", y = "0", height="70", width= "200")
        self.root.geometry("1300x700")
        self.canvas = Canvas(self.frame)
        self.canvas.config(height = sizeFrameY, width = sizeFrameX)
        self.canvas.place(x = 0, y = 0)
        self.dataImagesMap = None


    def drawImageNamesMatrix(self, imageNamesMatrix, sizeImageArray):
        self.dataImagesMap = Basic().paintImageNamesMatrixInCanvas(self.canvas,
        imageNamesMatrix, sizeImageArray)
        self.canvas = self.dataImagesMap["canvas"]
        self.root.mainloop()
