

from tkinter import *
from PIL import Image, ImageTk

class PaintImageNamesMatrixInCanvasTK:

    def inner(self, canvas, imageNamesMatrix,
    sizeImageArray):
        imageName = ""
        locationX = 0
        locationY = 0
        imageSizeX = sizeImageArray[1]
        imageSizeY = sizeImageArray[0]
        imageOpen = None
        vimage = None
        matrixImages = []
        arrayPhotoImage = []
        finalImageArray = []
        for y in range(len(imageNamesMatrix)):
            for x in range(len(imageNamesMatrix[y])):
                for i in range(len(imageNamesMatrix[y][x])):
                    imageName = imageNamesMatrix[y][x][i]
                    imageOpen = Image.open(imageName)
                    vimage = ImageTk.PhotoImage(imageOpen)
                    arrayPhotoImage.append(vimage)
                    finalImageArray.append(canvas.create_image(locationX,
                    locationY, anchor=NW, image=vimage))
                locationX += imageSizeX
            locationX = 0
            locationY += imageSizeY
        map = dict()
        map["photo_image_reference"] = arrayPhotoImage
        map["final_image_reference"] = finalImageArray
        map["canvas"] = canvas
        return map
