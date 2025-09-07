



from data_access.core.keys_data.KeysData import KeysData

class ResourceList:

    MARKET_GLOBAL_KEYS = KeysData().getMarketGlobalKeysMap()
    RESOURCES_KEYS = KeysData().getResourcesTypeMap()
    MARKET_LOCAL_KEYS = KeysData().getMarketGlobalKeysMap()

    def __init__(self):
        self.INNER = []
        return

    def addResource(self, location, type, quantity):
        array = [None] * 3
        if(location == "global"):
            array[1] = ResourceList.MARKET_GLOBAL_KEYS[type]
        elif(location == "local"):
            array[1] = ResourceList.MARKET_GLOBAL_KEYS[type]
        elif(location == "resource"):
            array[1] = ResourceList.RESOURCES_KEYS[type]
        array[2] = quantity
        self.INNER.append(array)

    def searshTheProductIndex(self, codeInt):
        for i in range(len(self.INNER)):
            if(self.INNER[i][1] == codeInt):
                return i
        return -1

    def hasTheProduct(self, codeInt):
        for i in range(len(self.INNER)):
            if(self.INNER[i][1] == codeInt):
                return True
        return False

    def obtainQuantityProduct(self, codeInt):
        for i in range(len(self.INNER)):
            if(self.INNER[i][1] == codeInt):
                return self.INNER[i][2]
