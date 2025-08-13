


class Capture:
    
    def __init__(self):
        self.capture_prob:float = 0
        self.necessary_baits:str = []
        self.description:str = ""
        self.value:int = 0

    def load_capture_dict(self, DICT):
        self.capture_prob\
            = DICT["CAPTURE_PROB"]
        self.necessary_baits\
            = DICT["NESESSARY_BAITS"]
        self.description \
            = DICT["DESCRIPTION"]
        self.value \
            = DICT["VALUE"]