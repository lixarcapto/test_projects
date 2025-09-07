
from btpy.Btpy import Btpy

def randomize_gender(data):
    KEY = Btpy.random_choice([
            "male", "female"
        ])
    data.set_gender_key(KEY)
    return data