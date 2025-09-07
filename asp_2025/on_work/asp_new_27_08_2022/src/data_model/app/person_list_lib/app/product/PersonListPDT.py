




class PersonListPDT:

    def __init__(self):
        self.personArray = []
        self.deadArray = []
        return

    def isVoid(self):
        if(0 < len(self.personArray)):
            return False
        return True

    def clean(self):
        self.personArray.clean()
