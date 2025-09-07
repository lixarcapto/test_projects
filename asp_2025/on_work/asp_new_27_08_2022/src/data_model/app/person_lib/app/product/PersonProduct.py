

from data_model.app.body_lib.PersonBody import PersonBody
from data_model.app.mind_lib.Mind import Mind
from data_model.app.general_lib.core.coordinate.Coordinate import Coordinate

class PersonProduct:

    def __init__(self):
        self.body = PersonBody()
        self.mind = Mind()
        self.coordinate = Coordinate()
        return
