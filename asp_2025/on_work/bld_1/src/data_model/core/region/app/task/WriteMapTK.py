

from data_model.core.terrain.Terrain import Terrain
from data_access.DataAccess import DataAccess
from basic.Basic import Basic

class WriteMapTK:

    def inner(self, regionPDT):
        textFinal = "  "
        translation = DataAccess().getTranslation()
        code = 0
        sizeBlockX = 15
        sizeBlockY = 4
        sizeBlockXAtHalf = int(sizeBlockX /2)
        spaceBlockInX = " " * sizeBlockXAtHalf
        terrain = Terrain()
        basic = Basic()
        for i in range(regionPDT.getSizeY()):
            textFinal +=  spaceBlockInX + str(i) + spaceBlockInX
        textFinal += "\n\n"
        for y in range(regionPDT.getSizeY()):
            textFinal +=  str(y) + "  "
            for x in range(regionPDT.getSizeX()):
                terrain = regionPDT.mapMatrix[y][x]
                code = terrain.inner.getBuildTypeInt()
                text = translation.translateBuildingType(code)
                text = basic.fullfillText(text, sizeBlockX)
                textFinal += "[" + text + "]"
            textFinal += "\n   "
            for x in range(regionPDT.getSizeX()):
                terrain = regionPDT.mapMatrix[y][x]
                code = terrain.inner.getResourceTypeInt()
                text = translation.translateResourceType(code)
                text = basic.fullfillText(text, sizeBlockX)
                textFinal += "[" + text + "]"
            textFinal += "\n   "
            for x in range(regionPDT.getSizeX()):
                terrain = regionPDT.mapMatrix[y][x]
                text = str(terrain.inner.getResourceQuantityInt())
                text = basic.fullfillText(text, sizeBlockX)
                textFinal += "[" + text + "]"
            textFinal += "\n   "
            for x in range(regionPDT.getSizeX()):
                terrain = regionPDT.mapMatrix[y][x]
                code = terrain.inner.getSoilTypeInt()
                text = translation.translateSoilType(code)
                text = basic.fullfillText(text, sizeBlockX)
                textFinal += "[" + text + "]"
            textFinal += "\n\n"
        return textFinal
