

from basic.core.image_popup.ImageOrder import ImageOrder

class PaintOrder:
    """
        Clase para la creacion de ordenes de dibujo complejas.
        Permite añadir imagenes para dibujar y luego enviarlas a un
        pintador de paintOrder.
        Las imagenes se crean llamando un imageOrder con su coordenada,
        y luego añadiendoles layouts con su propio tipoDeOrden que
        pueden ser texto, imagen, rectangulos, etc.
    """
    ORDER_TYPE = [
    "text",
    "image",
    "rectangle"
    ]

    def __init__(self):
        self.inner = []
        return

    """
        La imageDataArray contiene una matriz con el valor 0 imageName y
        1 orderType
    """
    def imageOrder(self, locationArray):
        return ImageOrder(locationArray)

    def addImage(self, imageOrder):
        map = dict()
        map["locationX"] = imageOrder.locationX
        map["locationY"] = imageOrder.locationY
        map["imageDataArray"] = imageOrder.imageDataArray
        self.inner.append(map)

    def addSerieImage(self, imageOrder, spaces, axe, quantity):
        locationX = imageOrder.locationX
        locationY = imageOrder.locationY
        for i in range(quantity):
            imageOrder.locationX = locationX
            imageOrder.locationY = locationY
            self.addImage(imageOrder)
            if(axe == "y"):
                locationY += spaces
            else:
                locationX += spaces

    """
        Recibe una matrix con nombre de imagen y un texto para
        convertirla en ordenes de imagen. Tambien requiere el tamaño del icono
        y la locacion de la lista
    """
    def addIconListArrayAsImages(self, iconListMatrix, sizeIconArray,
    locationListArray, quantityInY, distance):
        sizeIconX = sizeIconArray[1]
        sizeIconY = sizeIconArray[0]
        imageOrder = None
        locationY = locationListArray[0]
        locationX = locationListArray[1]
        counterInY = 0
        for i in range(len(iconListMatrix)):
            imageOrder = self.imageOrder([locationY, locationX])
            imageOrder.addLayoutImage(iconListMatrix[i][0], "image")
            self.addImage(imageOrder)
            imageOrder = self.imageOrder([locationY, locationX + sizeIconX])
            imageOrder.addLayoutImage(iconListMatrix[i][1], "text")
            self.addImage(imageOrder)
            if(counterInY == quantityInY -1):
                locationX += distance
                counterInY = 0
                locationY = locationListArray[0]
            else:
                locationY += sizeIconY
                counterInY += 1
