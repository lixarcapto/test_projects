


from data_access.app.names.product.NamesMaleMatrixData import NamesMaleMatrixData
from data_access.app.names.product.NamesFemaleMatrixData import NamesFemaleMatrixData
from data_access.app.names.product.LastnameHighCasteMatrixData import LastnameHighCasteMatrixData
from data_access.app.names.product.LastnameMidCasteMatrixData import LastnameMidCasteMatrixData
from data_access.app.names.product.RegionNamesMatrixData import RegionNamesMatrixData

class NamesData:

    def getLastnameHighCasteMatrix(self):
        return LastnameHighCasteMatrixData().INNER

    def getLastnameMidCasteMatrix(self):
        return LastnameMidCasteMatrixData().INNER

    def getNamesFemaleMatrix(self):
        return NamesFemaleMatrixData().INNER

    def getNamesMaleMatrix(self):
        return NamesMaleMatrixData().INNER

    def getRegionNamesMatrix(self):
        return RegionNamesMatrixData().INNER
