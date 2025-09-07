




class ExtractNearbyResourceTK:

    def inner(self, regionPDT, coordinateArray, resourceCode, quantity):
        regionMatrix = regionPDT.regionMatrix
        coordinateY = coordinateArray[0]
        coordinateX = coordinateArray[1]
        coordinateToReviewX = 0
        coordinateToReviewY = 0
        if(not self.isInitX([coordinateY, coordinateX])):
            if(regionMatrix[coordinateY][coordinateX -1].inner.resourceCode
            == resourceCode):
                regionMatrix[coordinateY][coordinateX -1].inner.resourceQuantity -= quantity
        if(not self.isInitY([coordinateY, coordinateX])):
            if(regionMatrix[coordinateY -1][coordinateX].inner.resourceCode
            == resourceCode):
                regionMatrix[coordinateY -1][coordinateX].inner.resourceQuantity -= quantity
        if(not self.isLimitX([coordinateY, coordinateX])):
            if(regionMatrix[coordinateY][coordinateX +1].inner.resourceCode
            == resourceCode):
                regionMatrix[coordinateY][coordinateX +1].inner.resourceQuantity -= quantity
        if(not self.isLimitY([coordinateY, coordinateX])):
            if(regionMatrix[coordinateY +1][coordinateX].inner.resourceCode
            == resourceCode):
                regionMatrix[coordinateY +1][coordinateX].inner.resourceQuantity -= quantity
        regionPDT.regionMatrix = regionMatrix
        return regionPDT
