

from ..const.age_range_dict import*

def get_age_range_gender(GENDER, 
            AGE_RANGE)->str:
        if(GENDER == "female"):
            return AGE_RANGE_FEMALE[AGE_RANGE]
        else:
            return AGE_RANGE_MALE[AGE_RANGE]