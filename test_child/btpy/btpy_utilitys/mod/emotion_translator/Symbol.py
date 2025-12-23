


class Symbol:

    def __init__(self):
        self.anger:str = ""
        self.joy:str = ""
        self.fear:str = ""
        self.disgust:str = ""
        self.boredom:str = ""
        self.sadness:str = ""

    def load_symbol_dict(self, symbol_dict):
        symbol = symbol_dict
        self.anger = symbol["anger"]
        self.joy = symbol["joy"]
        self.fear = symbol["fear"]
        self.disgust = symbol["disgust"]
        self.boredom = symbol["boredom"]
        self.sadness = symbol["sadness"]
