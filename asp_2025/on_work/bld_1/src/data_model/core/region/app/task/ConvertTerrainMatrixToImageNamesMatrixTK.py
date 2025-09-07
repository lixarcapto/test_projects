


from basic.Basic import Basic
from data_access.DataAccess import DataAccess

class ConvertTerrainMatrixToImageNamesMatrixTK:

    def inner(self, regionPDT, camLocationY,
    camLocationX, sizeDistrict, actualDistrictSelected):
        code = 0
        text = ""
        directionImages = "/Users/luisd/OneDrive/Escritorio/"
        directionImages += "py_proyects/bld_1/res/image/"
        translation = DataAccess().getTranslation()
        keysData = DataAccess().getKeysData()
        cuttedMatrix = Basic().cutMatrix3D(regionPDT.mapMatrix,
        camLocationY, camLocationX,
        sizeDistrict, sizeDistrict)
        matrixOfString = Basic().matrix([len(cuttedMatrix), len(cuttedMatrix[0])])
        array = None
        sizeText = 15
        colorText = ""
        format = ".png"
        resourceCollection = DataAccess().getResourceCollection()
        imageNameStringMatrix = Basic().matrix([len(cuttedMatrix),
        len(cuttedMatrix[0])])
        for y in range(len(cuttedMatrix)):
            for x in range(len(cuttedMatrix[0])):
                imageNameStringMatrix[y][x] = []
                code = cuttedMatrix[y][x].inner.getSoilTypeInt()
                text = keysData.getSoilTypeKey(code)
                text = directionImages + "region/type_soil_terrain/"+text + format
                imageNameStringMatrix[y][x].append(text)
                code = cuttedMatrix[y][x].inner.getResourceTypeInt()
                text = resourceCollection.getResourceByIndex(code).basicImageName
                text = directionImages + text + format
                imageNameStringMatrix[y][x].append(text)
                """
                text = ""
                text += "y" + str(cuttedMatrix[y][x].inner.locationY)
                text += "x" + str(cuttedMatrix[y][x].inner.locationX)
                text = Basic().fullfillText(text, sizeText)
                matrixOfString[y][x][4] += text
                """
        """
        titleMap = "region: " + str(self.inner.getCode())
        titleMap += "district: " +str(actualDistrictSelected)+ "\n"
        """
        return imageNameStringMatrix
