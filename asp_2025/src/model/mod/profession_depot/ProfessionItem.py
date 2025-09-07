



class ProfessionItem:

    def __init__(self, DICT):
        self.__carried_object:str = ""
        self.__cause_death_list\
            :list[str] = []
        self.__activities_list\
            :list[str] = []
        self.__death_probability\
            :float = 0.0
        self.convert_profession_dict(DICT)
        
    def get_carried_object(self)->str:
        return self.__carried_object
    
    def get_cause_death_list(self)->list:
        return self.__cause_death_list
    
    def get_activities_list(self)->list:
        return self.__activities_list
    
    def get_death_probability(self)->float:
        return self.__death_probability
        
    def convert_profession_dict(self,
            DICT:dict):
        self.__carried_object \
            = DICT["CARRIED_OBJECT"]
        self.__cause_death_list\
            = list(DICT["CAUSE_DEATH_LIST"])
        self.__activities_list\
            = list(DICT["ACTIVITIES_LIST"])
        self.__death_probability\
            = float(DICT["DEATH_PROBABILITY"])