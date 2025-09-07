


from data_access.DataAccess import DataAccess

class RaceProduct:

    def __init__(self):
        self.PERSON_KEYS = DataAccess().getPersonData()
        self.keyCode = 0
        self.hairColorPosibleArray = []
        self.eyeTypePosibleArray = []
        self.heightPosibleArray = []
        self.skinColorPosibleArray = []
        self.eyeColorPosibleArray = []
        self.hairTypePosibleArray = []
