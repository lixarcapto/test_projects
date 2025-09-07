


class Resource:

    def __init__(self) -> None:
        self.type = ""
        self.life_time = 0
        self.production = 0

    def describe(self):
        txt = ""
        txt += self.type
        return txt