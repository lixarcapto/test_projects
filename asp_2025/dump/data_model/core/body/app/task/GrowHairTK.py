


from data_access.DataAccess import DataAccess

class GrowHairTK:

    def inner(self, bodyProduct):
        valuesSupplier = DataAccess().createValuesSupplier()
        if(bodyProduct.getHairStyle() <= valuesSupplier.getHairStyleKeyMapLimit() -1):
            height = bodyProduct.getHairStyle() + 1
            bodyProduct.setHairStyle(height)
        if(bodyProduct.getFacialHairStyle() <= valuesSupplier.getFacialHairStyleKeyMapLimit() -1
        and bodyProduct.getGender() == 0):
            height = bodyProduct.getFacialHairStyle() + 1
            bodyProduct.setFacialHairStyle(height)
        elif(bodyProduct.getFacialHairStyle() <= 2
        and bodyProduct.getGender() == 1):
            height = bodyProduct.getFacialHairStyle() + 1
            bodyProduct.setFacialHairStyle(height)
        return bodyProduct
