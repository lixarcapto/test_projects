



from data_access.core.resource_list.ResourceList import ResourceList

class RecipeEntity:

    def __init__(self):
        self.extractResources = False
        self.resourceExtractionList = ResourceList()
        self.requerimentList = ResourceList()
        self.productionList = ResourceList()
        self.key = ""
        return
