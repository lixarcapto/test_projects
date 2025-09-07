


from ..society.Society import Society
from ..market.Market import Market
from .RegionData import RegionData

from .mod.write_narrative_region import*

class Region:

    """
    Clase que representa a una region 
    geografica especifica. Esta simula
    ser una region del tamaño de un estado.
    En el futuro debe contener distritos.
    Puede o no estar habitada.
    """

    def  __init__(self):
        self.d = RegionData()

    def write_narrative(self)->str:
        return write_narrative_region(self.d)

    def has_person(self, ID):
        return self.d.society.has_with_id(ID)
    
    def get_all_character_id(self)\
            ->list[int]:
        return self.d.society\
            .get_all_character_id()
    
    def get_person(self, ID):
        return self.d.society.get_by_id(ID)
    
    def get_description(self, ID):
        description = self.d.society\
            .get_description(ID)
        description.region_text = self\
            .write_narrative()
        return description
    
    def advance_one_day(self):
        if(self.d.get_is_inhabited()):
            self.d.society.advance_one_day()

    def occupy(self, quantity:int, 
            culture:str):
        """
        Crea una sociedad al interior; 
        ocupando el territorio con personas.
        """
        self.d.society = Society()
        self.d.society.create_group(
            quantity, culture, 
            self.d.get_number())
        self.d.set_is_inhabited(True)