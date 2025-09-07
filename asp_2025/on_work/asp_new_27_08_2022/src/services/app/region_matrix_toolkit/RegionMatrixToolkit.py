



class RegionMatrixToolkit:

    def createMatrix(self, regionMatrix):
        citizenLimit = 50
        n = 0
        regionMatrix = [None] * regionMatrix.SIZE_Y
        for i in range(regionMatrix.SIZE_Y):
            regionMatrix[i] = [None] * regionMatrix.SIZE_X
        for y in range(regionMatrix.SIZE_Y):
            for x in range(regionMatrix.SIZE_X):
                self.regionMatrix[y][x] = regionMatrix.createRegion(citizenLimit)
                self.regionMatrix[y][x].traits.code = n
                self.regionMatrix[y][x].traits.locationX = x
                self.regionMatrix[y][x].traits.locationY = y
                n += 1
        return regionMatrix
