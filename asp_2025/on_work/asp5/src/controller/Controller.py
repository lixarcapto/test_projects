


from model.Model import Model
import os

class Controller:

    def __init__(self):
        self.model = Model()
        self.start()

    def start(self):
        text_to_print = ""
        user_input = ""
        while(True):
            os.system ("cls")
            text_to_print = self.model.write()
            print(text_to_print)
            user_input = input()
            if(user_input == "f"
            or user_input == "end"):
                break
            self.model.advance_time()
