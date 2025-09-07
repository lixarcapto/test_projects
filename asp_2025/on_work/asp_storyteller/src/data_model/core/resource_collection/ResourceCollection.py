


from data_model.core.resource_collection.app.entities.ResourceNone import ResourceNone
from data_model.core.resource_collection.app.entities.ResourceForestCamp import ResourceForestCamp
from data_model.core.resource_collection.app.entities.ResourceForestOak import ResourceForestOak
from data_model.core.resource_collection.app.entities.ResourceStoneMassif import ResourceStoneMassif
from data_model.core.resource_collection.app.entities.HydrocarbonsDeposit import HydrocarbonsDeposit

class ResourceCollection:

    def __init__(self):
        self.inner = dict()
        self.addResource(ResourceNone())
        self.addResource(ResourceForestCamp())
        self.addResource(ResourceForestOak())
        self.addResource(ResourceStoneMassif())
        self.addResource(HydrocarbonsDeposit())
        return

    def addResource(self, resource):
        self.inner[resource.inner.getKeyname()] = resource
