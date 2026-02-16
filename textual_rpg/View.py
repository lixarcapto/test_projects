

from Model import Model

class View:

    def __init__(self):
        self.model = Model()
        self.start_loop()

    def start_loop(self):
        user_input = ""
        output = ""
        while(True):
            user_input = input(output)
            if(user_input == "f"):
                break
            elif(user_input == ""):
                self.model\
                    .advance_one_turn()
            output = self.model.write()
            print("\n")