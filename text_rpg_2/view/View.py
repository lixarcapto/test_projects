

from btpy.Btpy import Btpy
from model.Model import Model

class View:

    def __init__(self):
        self.model = Model()
        user_input = ""
        output = ""
        while(True):
            output = self.model\
                .render()["PLAYER"]
            user_input = input(output)
            if(user_input == "f"):
                break
            if("move" in user_input):
                list_ = user_input.split(
                    ":"
                )
                self.model.request(
                    {
                        "ORDER":list_[0],
                        "INDEX":int(list_[1])
                    }
                )