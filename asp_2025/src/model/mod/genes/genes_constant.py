
from persistence.Persistence import Persistence

DICT_ = Persistence\
            .read_genetic_keys_dict()

ALBINISM_PROBABILITY:int\
    = int(DICT_["ALBINISM_PROBABILITY"][0])

INFERTILITY_PROBABILITY:int\
    = int(DICT_["INFERTILITY_PROBABILITY"][0])

EYE_COLOR_K_TUPLE:tuple[str]\
    = DICT_["EYE_COLOR_KEY_LIST"]

EYE_TYPE_K_TUPLE:tuple[str]\
    = DICT_["EYE_TYPE_KEY_LIST"]

SKIN_COLOR_K_TUPLE:tuple[str]\
    = DICT_["SKIN_COLOR_KEY_LIST"]

HAIR_COLOR_K_TUPLE:tuple[str]\
    = DICT_["HAIR_COLOR_KEY_LIST"]

HAIR_TYPE_K_TUPLE:tuple[str]\
    = DICT_["HAIR_TYPE_KEY_LIST"]

HEIGHT_MAX_KEY_TUPLE:tuple[str]\
    = DICT_["HEIGHT_MAX_KEY_LIST"]

NOSE_TYPE_KEY_TUPLE:list[str]\
    = DICT_["NOSE_TYPE_KEY_LIST"]

MOUTH_TYPE_KEY_TUPLE:list[str]\
    = DICT_["MOUTH_TYPE_KEY_LIST"]
