

from Pet import Pet

class Model:

    def __init__(self):
        self.pet = Pet()

    def feed(self):
        self.pet.feed()
        self.pet.update()

    def offend(self):
        self.pet.offend()
        self.pet.update()