


class RegionalGroupItem:

    def __init__(self, DICT:dict):
        self.__clothing_style_list\
            :list[str] = []
        self.__hairstyle_list\
            :list[str] = []
        self.__eye_color_list\
            :list[str] = []
        self.__skin_color_list\
            :list[str] = []
        self.__eye_type_list\
            :list[str] = []
        self.__height_maximum_list\
            :list[str] = []
        self.__hair_color_list\
            :list[str] = []
        self.__hair_type_list\
            :list[str] = []
        self.__freckles_probability\
            :float = 0.0
        self.__baldness_probability\
            :float = 0.0
        self.__nose_type_list\
            :list[str] = []
        self.__mouth_type_list\
            :list[str] = []
        self.load_regional_group_dict(DICT)
        
    def load_regional_group_dict(self, 
            DICT:dict):
        self.__clothing_style_list\
            = DICT["clothing_style_key"]
        self.__hairstyle_list\
            = DICT["hairstyle_key"]
        self.__eye_color_list\
            = DICT["eye_color_key"]
        self.__skin_color_list\
            = DICT["skin_color_key"]
        self.__eye_type_list\
            = DICT["eye_type_key"]
        self.__height_maximum_list\
            = DICT["height_maximum_key"]
        self.__hair_color_list\
            = DICT["hair_color_key"]
        self.__hair_type_list\
            = DICT["hair_type_key"]
        v = DICT["freckles_probability"]
        self.__freckles_probability\
            = float(v[0])
        v = DICT["baldness_probability"]
        self.__baldness_probability\
            = float(v[0])
        self.__nose_type_list\
            = DICT["nose_type_key"]
        self.__mouth_type_list\
            = DICT["mouth_type_key"]
        
    def get_clothing_style_list(self)\
            ->list:
        return self.__clothing_style_list
    
    def get_hairstyle_list(self)->list:
        return self.__hairstyle_list
    
    def get_eye_color_list(self)->list:
        return self.__eye_color_list
    
    def get_skin_color_list(self)->list:
        return self.__skin_color_list
    
    def get_eye_type_list(self)->list:
        return self.__eye_type_list
    
    def get_height_maximum_list(self)\
            ->list:
        return self.__height_maximum_list

    def get_hair_color_list(self)->list:
        return self.__hair_color_list
    
    def get_hair_type_list(self)->list:
        return self.__hair_type_list

    def get_freckles_probability(self)\
            ->float:
        return self.__freckles_probability
    
    def get_baldness_probability(self)\
            ->float:
        return self.__baldness_probability
    
    def get_nose_type_list(self)->list:
        return self.__nose_type_list
    
    def get_mouth_type_list(self)->list:
        return self.__mouth_type_list