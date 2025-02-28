

from ....btpy_persistence.mod.read_nested_row_xlsx.read_nested_row_xlsx import*
from .Symbol import Symbol

class EmotionTranslator:

    def __init__(self):
        self.__symbol_object_dict = {}

    def has_word(self, word:str):
        return word in self\
            .__symbol_object_dict

    def load_data_base_symbol(self, path):
        nestdict = read_nested_row_xlsx(
            path)
        self.load_symbol_nestdict(nestdict)

    def get_symbol(self, key):
        return self.__symbol_object_dict[key]

    def load_symbol_nestdict(self, 
            symbol_nestdict):
        for k in symbol_nestdict:
            self.__add_symbol_dict(
                k, symbol_nestdict[k])
            
    def __add_symbol_dict(self, 
            key, symbol_dict):
        symbol = Symbol()
        symbol.load_symbol_dict(
            symbol_dict)
        self.__symbol_object_dict[key]\
            = symbol
            