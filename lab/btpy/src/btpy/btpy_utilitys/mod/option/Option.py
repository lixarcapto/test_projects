

from ..decision_three.DecisionThree import DecisionThree

class Option:

    def __init__(self) -> None:
        self.decision = DecisionThree()
        self.data_index_dict = {}
        self.key_register = []

    def add_node(self, key, data = "", 
                link_arr = []):
        self.data_index_dict[key] = data
        self.decision.add_node(key, link_arr)

    def reset(self):
        self.decision.reset()
        self.key_register.clear()

    def write(self):
        txt = ""
        key = self.decision.get_key()
        key_list = self.decision.get_next_key()
        txt += self.data_index_dict[key] + "\n"
        for i, e in enumerate(key_list, 
                start=1):
            txt += f"{i}). {e}\n"
        return txt

    def start(self):
        while(self.decision.has_next()):
            print(self.write())
            us_input = input()
            if(us_input == "f"): break
            us_input = int(us_input) - 1
            self.decision.set_key_by_index(
                us_input)
            self.key_register.append(
                self.decision.get_key())
        print(str(self.key_register))
