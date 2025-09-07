

from model.Model import Model
import os

class View:

    def __init__(self):
        self.model = Model()

    def start(self):
        us_input = ""
        on_wait = "talk with he"
        self.model.create_world()
        while(True):
            self.clean()
            self.print(on_wait)
            us_input = self.catch()
            if(us_input == "bye"):
                break
            on_wait = self.model\
                .talk(us_input)

    def print(self, text:str):
        print(text)

    def catch(self):
        return input()
    
    def clean(self):
        os.system("cls")