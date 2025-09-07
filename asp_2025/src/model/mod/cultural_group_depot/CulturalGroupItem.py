


class CulturalGroupItem:

    def __init__(self, DICT:dict):
        self.__demonym:str = ""
        self.__regional_group_list\
            :list["str"] = []
        self.__ideology_list\
            :list["str"] = []
        self.__hairstyle_female_list\
            :list["str"] = []
        self.__hairstyle_male_list\
            :list["str"] = []
        self.__key_names:str = ""
        self.__beard_style_female_list\
            :list["str"] = []
        self.__beard_style_male_list\
            :list["str"] = []
        self.__makeup_female_list\
            :list["str"] = []
        self.__makeup_male_list\
            :list["str"] = []
        self.convert_cultural_group_dict(
            DICT
        )
        
    def convert_cultural_group_dict(self, 
            DICT:dict):
        self.__demonym\
            = DICT["demonym"][0]
        self.__regional_group_list\
            = DICT["regional_group_key"]
        self.__ideology_list\
            = DICT["ideology_key"]
        self.__hairstyle_female_list\
            = DICT["hairstyle_female"]
        self.__hairstyle_male_list\
            = DICT["hairstyle_male"]
        self.__key_names\
            = DICT["key_names"][0]
        self.__beard_style_female_list\
            = DICT["beard_style_female"]
        self.__beard_style_male_list\
            = DICT["beard_style_male"]
        self.__makeup_female_list\
            = DICT["makeup_female_list"]
        self.__makeup_male_list\
            = DICT["makeup_male_list"]
        
    def get_demonym(self)->str:
        return self.__demonym
    
    def get_regional_group_list(self)->str:
        return self.__regional_group_list
    
    def get_ideology_list(self)->str:
        return self.__ideology_list

    def get_hairstyle_female_list(self)\
            ->str:
        return self.__hairstyle_female_list
    
    def get_hairstyle_male_list(self)->str:
        return self.__hairstyle_male_list
    
    def get_key_names(self)->str:
        return self.__key_names
    
    def get_beard_style_female_list(self)\
            ->list:
        return self.__beard_style_female_list
    
    def get_beard_style_male_list(self)\
            ->list:
        return self.__beard_style_male_list
    
    def get_makeup_female_list(self)\
            ->list:
        return self.__makeup_female_list
    
    def get_makeup_male_list(self)->list:
        return self.__makeup_male_list
