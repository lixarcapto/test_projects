

from data_model.app.region_lib.core.terrain.Terrain import Terrain

class TerrainMatrix:

    SIZE_TERRAIN = 10

    def __init__(self):
        self.terrainMatrix = [None] * TerrainMatrix.SIZE_TERRAIN
        n = 0
        for i in range(TerrainMatrix.SIZE_TERRAIN):
            self.terrainMatrix[i] = [None] * TerrainMatrix.SIZE_TERRAIN
        for y in range(TerrainMatrix.SIZE_TERRAIN):
            for x in range(TerrainMatrix.SIZE_TERRAIN):
                self.terrainMatrix[x][y] = Terrain()
                self.terrainMatrix[x][y].indexX = x
                self.terrainMatrix[x][y].indexY = y
                self.terrainMatrix[x][y].code = n
                n += 1

    def getTerrainByCode(self, code):
        for y in range(TerrainMatrix.SIZE_TERRAIN):
            for x in range(TerrainMatrix.SIZE_TERRAIN):
                if(self.terrainMatrix[x][y].code == code):
                    return self.terrainMatrix[x][y]
        return None

    def setTerrain(self, terrainProduct):
        self.terrainMatrix[terrainProduct.indexX][terrainProduct.indexY] = terrainProduct
