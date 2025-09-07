


from persistence.Persistence import Persistence

DICT = Persistence.read_world_const()

QUANTITY_ZONES:int \
    = DICT["QUANTITY_ZONES"][0]
MAX_INITIAL_TOWNS:int \
    = DICT["MAX_INITIAL_TOWNS"][0]
MAX_HEIGHT_ZONES:int \
    = DICT["MAX_HEIGHT_ZONES"][0]
MIN_HEIGHT_ZONES:int \
    = DICT["MIN_HEIGHT_ZONES"][0]
MIN_INITIAL_TOWNS:int \
    = DICT["MIN_INITIAL_TOWNS"][0]
