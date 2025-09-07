



class ImageOrder:

    def __init__(self, locationArray):
        self.inner = dict()
        self.locationX = locationArray[1]
        self.locationY = locationArray[0]
        self.imageDataArray = []
        return

    def addLayoutImage(self, nameImage, orderType):
        array = []
        array.append(nameImage)
        array.append(orderType)
        self.imageDataArray.append(array)
