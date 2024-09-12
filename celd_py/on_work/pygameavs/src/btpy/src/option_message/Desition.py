

class Desition:

    def __init__(self, id:str) -> None:
        self.id = id
        self.text = ""
        self.option_id = []

    def write(self):
        txt = f"{self.id}\n{self.text}\n"
        txt += f"{self.option_id}\n"
        return txt

    def write_narrative(self):
        txt = f"{self.text}\n"
        i = 1
        for e in self.option_id:
            txt += " " * 2 
            txt += f"{i}.{e}\n"
            i += 1
        return txt