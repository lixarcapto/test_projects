




from data_access.core.collection_supplier.app.entities.races_entities.RaceArabMap import RaceArabMap
from data_access.core.collection_supplier.app.entities.races_entities.RaceAsianMap import RaceAsianMap
from data_access.core.collection_supplier.app.entities.races_entities.RaceCelticMap import RaceCelticMap
from data_access.core.collection_supplier.app.entities.races_entities.RaceGermanicMap import RaceGermanicMap
from data_access.core.collection_supplier.app.entities.races_entities.RaceIndianMap import RaceIndianMap
from data_access.core.collection_supplier.app.entities.races_entities.RaceIndoamericanMap import RaceIndoamericanMap
from data_access.core.collection_supplier.app.entities.races_entities.RaceMediterraneanMap import RaceMediterraneanMap
from data_access.core.collection_supplier.app.entities.races_entities.RaceMongolianMap import RaceMongolianMap
from data_access.core.collection_supplier.app.entities.races_entities.RaceNordicMap import RaceNordicMap
from data_access.core.collection_supplier.app.entities.races_entities.RacePolynesianMap import RacePolynesianMap
from data_access.core.collection_supplier.app.entities.races_entities.RaceSahelineMap import RaceSahelineMap
from data_access.core.collection_supplier.app.entities.races_entities.RaceSlavsMap import RaceSlavsMap
from data_access.core.collection_supplier.app.entities.races_entities.RaceSubsaharanMap import RaceSubsaharanMap
from data_access.core.collection_supplier.app.entities.races_entities.RaceTurkishMap import RaceTurkishMap

class RaceCollection:

    def __init__(self):
        self.collectionArray = []
        self.collectionArray.append(RaceNordicMap().INNER)
        self.collectionArray.append(RaceMediterraneanMap().INNER)
        self.collectionArray.append(RaceGermanicMap().INNER)
        self.collectionArray.append(RaceCelticMap().INNER)
        self.collectionArray.append(RaceSlavsMap().INNER)
        self.collectionArray.append(RaceArabMap().INNER)
        self.collectionArray.append(RaceSubsaharanMap().INNER)
        self.collectionArray.append(RaceTurkishMap().INNER)
        self.collectionArray.append(RaceMongolianMap().INNER)
        self.collectionArray.append(RaceAsianMap().INNER)
        self.collectionArray.append(RaceSahelineMap().INNER)
        self.collectionArray.append(RacePolynesianMap().INNER)
        self.collectionArray.append(RaceIndoamericanMap().INNER)
        self.collectionArray.append(RaceIndianMap().INNER)
        return
