


class AgeRangeItem:

    def __init__(self, AGE_RANGE_DICT):
        self.range_list:list = []
        self.death_probability = 0
        self.fertility = 0
        self.__baldness_probability:int = 0
        self.__gray_hair_probability\
            :int = 0
        self.load_age_range_dict(
            AGE_RANGE_DICT
        )

    def get_range_list(self)->list:
        return self.range_list
    
    def get_death_probability(self)->int:
        return self.death_probability
    
    def get_fertility(self)->int:
        return self.fertility
    
    def get_baldness_probability(self)\
            ->int:
        return self.__baldness_probability
    
    def get_gray_hair_probability(self)\
            ->int:
        return self.__gray_hair_probability

    def load_age_range_dict(self, dict_):
        self.range_list\
            = dict_["range_list"]
        self.death_probability\
            = dict_["death_probability"]
        self.fertility = dict_["fertility"]
        self.__baldness_probability\
            = dict_["baldness_probability"]
        self.__gray_hair_probability\
            = dict_["gray_hair_probability"]
