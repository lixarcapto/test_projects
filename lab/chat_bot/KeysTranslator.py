

from btpy.src.btpy.Btpy import*

class KeysTranslator:

    def __init__(self) -> None:
        self.keys_dict = {}
        self.keys_dict = Btpy.read_excel_dict(
            "./res/keys_words.xlsx")
        
    def translate_phrase(self, PHRASE):
        array = Btpy.get_words(PHRASE)
        keys_result = []
        for word in array:
            keys_result = keys_result \
                + self.translate_word(word)
        return keys_result

    def translate_word(self, WORD):
        if(WORD in self.keys_dict):
            return self.keys_dict[WORD]
        return []
