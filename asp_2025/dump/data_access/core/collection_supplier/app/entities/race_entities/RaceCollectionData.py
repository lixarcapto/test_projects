


from data_model.app.body_lib.core.race.app.entities.RaceNordicProduct import RaceNordicProduct
from data_model.app.body_lib.core.race.app.entities.RaceMediterraneanProduct import RaceMediterraneanProduct
from data_model.app.body_lib.core.race.app.entities.RaceAsianProduct import RaceAsianProduct
from data_model.app.body_lib.core.race.app.entities.RaceCelticProduct import RaceCelticProduct
from data_model.app.body_lib.core.race.app.entities.RaceGermanicProduct import RaceGermanicProduct
from data_model.app.body_lib.core.race.app.entities.RaceSlavsProduct import RaceSlavsProduct
from data_model.app.body_lib.core.race.app.entities.RaceArabProduct import RaceArabProduct
from data_model.app.body_lib.core.race.app.entities.RaceSubsaharanProduct import RaceSubsaharanProduct
from data_model.app.body_lib.core.race.app.entities.RaceTurkishProduct import RaceTurkishProduct
from data_model.app.body_lib.core.race.app.entities.RaceMongolianProduct import RaceMongolianProduct
from data_model.app.body_lib.core.race.app.entities.RaceSahelineProduct import RaceSahelineProduct
from data_model.app.body_lib.core.race.app.entities.RacePolynesianProduct import RacePolynesianProduct
from data_model.app.body_lib.core.race.app.entities.RaceIndoamericanProduct import RaceIndoamericanProduct
from data_model.app.body_lib.core.race.app.entities.RaceIndianProduct import RaceIndianProduct

class RaceCollectionData:

    def __init__(self):
        self.culturesArray = [None] * 14
        self.culturesArray[0] = RaceNordicProduct()
        self.culturesArray[1] = RaceMediterraneanProduct()
        self.culturesArray[2] = RaceGermanicProduct()
        self.culturesArray[3] = RaceCelticProduct()
        self.culturesArray[4] = RaceSlavsProduct()
        self.culturesArray[5] = RaceArabProduct()
        self.culturesArray[6] = RaceSubsaharanProduct()
        self.culturesArray[7] = RaceTurkishProduct()
        self.culturesArray[8] = RaceMongolianProduct()
        self.culturesArray[9] = RaceAsianProduct()
        self.culturesArray[10] = RaceSahelineProduct()
        self.culturesArray[11] = RacePolynesianProduct()
        self.culturesArray[12] = RaceIndoamericanProduct()
        self.culturesArray[13] = RaceIndianProduct()
