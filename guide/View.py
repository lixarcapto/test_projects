


from btpy.Btpy import Btpy
from Model import Model

class View:

    def __init__(self):
        self.model = Model()
        self.window = Btpy.Window(
            "titulo"
        )
        self.frame = Btpy.Frame(
            self.window)
        self.frame.pack()
        self.input_salary = Btpy.TextField(
            self.frame, " salary "
        )
        self.input_salary.grid(0, 0)
        self.showers_input = Btpy.TextField(
            self.frame, " showers in week "
        )
        self.showers_input.grid(0, 1)
        self.button_calculate = Btpy.Button(
            self.frame, "calculate")
        self.button_calculate.grid(0, 2)
        self.table = Btpy.Table(
            self.frame, True, "table"
        )
        self.table.grid(0, 3)
        self.add_default_listener()
        self.window.start()
        
    def add_default_listener(self):
        self.button_calculate\
            .add_listener(
                self.calculate
            )
        
    def get_input_salary(self):
        n = int(self.input_salary.get_value())
        return n
    
    def get_showers(self):
        n = int(self.showers_input.get_value())
        return n

    def calculate(self, e):
        self.model.profile_dict["salary"]\
            = self.get_input_salary()
        self.model.profile_dict[
            "showers_in_week"]\
            = self.get_showers()
        self.model.calculate()
        print(self.model.final_dict)
        