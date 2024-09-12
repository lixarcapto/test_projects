


from btpy.src.btpy.Btpy import Btpy
from LETTERS import LETTERS

class Model:

    LETTERS = {}

    def __init__(self) -> None:
        self.LETTERS = LETTERS
        self.translate_dict = {}
        self.result = ""

    def receive(self, message):
        if(message["command"] == "to_afi"):
            self.result = self.translate_to_ai(
                message["text"])
        
    def request(self):
        return {"text":self.result}

    def translate_to_ai(self, ORIGINAL_TEXT):
        translate_text = Btpy.replace_with_dict(
            ORIGINAL_TEXT, 
            self.LETTERS
        )
        return translate_text
