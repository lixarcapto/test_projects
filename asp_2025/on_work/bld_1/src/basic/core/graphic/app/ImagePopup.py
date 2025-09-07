
from tkinter import *
from basic.Basic import Basic
from PIL import Image, ImageTk
from basic.core.image_popup.PaintOrder import PaintOrder

class ImagePopup:

    """
        Componente grafico que recive paintOrder para dibujar imagenes en
        la pantalla temporal.
    """

    def __init__(self, sizeImageArray):
        self.paintOrder = PaintOrder()
        self.dataImagesMap = None
        sizeFrameX = sizeImageArray[1]
        sizeFrameY = sizeImageArray[0]
        #root
        self.root = None
        self.root = Tk()
        self.root.pack_propagate(False)
        self.root.grid_propagate(False)
        self.root.geometry("" + str(sizeFrameX) + "x" + str(sizeFrameY))
        #
        #frame
        self.frame = Frame(self.root, background = "yellow")
        self.frame.pack_propagate(False)
        self.frame.grid_propagate(False)
        self.frame.config(background = "yellow")
        self.frame.place(x = "0", y = "0", height=sizeFrameY, width=sizeFrameX)
        #
        #canvas
        self.canvas = Canvas(self.frame)
        self.canvas.config(height = sizeFrameY, width = sizeFrameX)
        self.canvas.place(x = 0, y = 0)
        #

    def createPaintOrder(self):
        return PaintOrder()

    def setPaintOrder(self, paintOrder):
        self.paintOrder = paintOrder

    def addImage(self, nameImageArray, locationArray):
        self.paintOrder.addImage(nameImageArray, locationArray)

    """
        Dibuja una serie de imagenes en linea o fila segun el eje
        indicado y o x.
    """
    def addSerieImage(self, nameImageArray, locationArray, spaces,
    axe, quantity):
        locationX = locationArray[1]
        locationY = locationArray[0]
        for i in range(quantity):
            self.addImage(nameImageArray, [locationY, locationX])
            if(axe == "y"):
                locationY += spaces
            else:
                locationX += spaces

    """
        dibuja una matriz de imagenes de paintOrder
    """
    def drawPaintOrder(self, canvas, paintOrder):
        imageNamesMatrix = paintOrder.inner
        imageName = ""
        imageNamesArray = None
        imageOpen = None
        vimage = None
        matrixImages = []
        arrayPhotoImage = []
        finalImageArray = []
        typeCommand = ""
        for i in range(len(imageNamesMatrix)):
            imageDataArray = imageNamesMatrix[i]["imageDataArray"]
            locationX = imageNamesMatrix[i]["locationX"]
            locationY = imageNamesMatrix[i]["locationY"]
            print(imageName)
            for e in imageDataArray:
                if(e[1] == "image"):
                    imageOpen = Image.open(e[0])
                    vimage = ImageTk.PhotoImage(imageOpen)
                    arrayPhotoImage.append(vimage)
                    finalImageArray.append(canvas.create_image(locationX,
                    locationY, anchor=NW, image=vimage))
                if(e[1] == "text"):
                    finalImageArray.append(canvas.create_text(locationX,
                    locationY, text= e[0]))
        map = dict()
        map["photo_image_reference"] = arrayPhotoImage
        map["final_image_reference"] = finalImageArray
        map["canvas"] = canvas
        return map

    """
        Dibuja un mapa segun el orden de la matriz.
    """
    def drawImageNamesMatrix(self, imageNamesMatrix, sizeImageArray):
        self.dataImagesMap = Basic().paintImageNamesMatrixInCanvas(self.canvas,
        imageNamesMatrix, sizeImageArray)
        self.canvas = self.dataImagesMap["canvas"]
        self.root.mainloop()

    """
        Finaliza la configuracion del componente y dibuja las imagenes
        para mostrarlas.
    """
    def drawImage(self):
        self.dataImagesMap = self.drawPaintOrder(self.canvas,
        self.paintOrder)
        self.canvas = self.dataImagesMap["canvas"]
        self.root.mainloop()

    def start(self):
        self.root.mainloop()
