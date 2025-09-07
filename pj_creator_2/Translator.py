


class Translator:

    lenguage_key:str = "english"

    def __init__(self, DICT = {}):
        self.__dict = {}
        self.set_dict(DICT)

    def set_dict(self, DICT):
        self.__dict = DICT

    def translate_key(self, 
            KEY:str):
        return self.__dict[KEY]\
            [Translator.lenguage_key]
    
    def get_text_list(self):
        list_ = []
        text = ""
        lenguage_key = Translator\
            .lenguage_key
        for k in self.__dict:
            text = self.__dict\
                    [k][lenguage_key]
            list_.append(text)
        return list_
    
    def get_keys(self):
        return list(self.__dict.keys())