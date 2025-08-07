
from btpy.Btpy import Btpy

class Pet:

    RES = "./res/"
    EXPRESION_RANGES = {
        "sad":[0, 5],
        "normal":[6, 10],
        "happy":[11, 15]
    }

    def __init__(self):
        self.category = "person"
        self.expression = "normal"
        self.emotion_value = 0
        self.energy = 0
        self.update()
        self.is_night = False
        self.create_pet()

    def create_pet(self):
        self.identify_time_of_day()
        self.emotion_value = Pet\
            .EXPRESION_RANGES["normal"][0]

    def update(self):
        self.identify_emotion()

    def identify_time_of_day(self):
        time = Btpy.Time(0,0,0,0)
        hour = time.get_actual_hour().hour
        if(hour > 18 or hour < 7):
            self.is_night = True
            self.expression = "sleep"

    def identify_emotion(self):
        self.expression = Btpy.whats_range(
            Pet.EXPRESION_RANGES,
            self.emotion_value
        )[0]
        if(self.energy == 0):
            self.expression = "sleep"

    def offend(self):
        self.emotion_value = Btpy\
            .sum_in_range(
                self.emotion_value, 
                1 *-1, 
                [0, 15]
            )

    def feed(self):
        self.emotion_value = Btpy\
            .sum_in_range(
                self.emotion_value, 
                1, 
                [0, 15]
            )
        self.energy = Btpy\
            .sum_in_range(
                self.energy, 
                1, 
                [0, 15]
            )

    def get_path_list(self):
        list_ = []
        list_.append(
            Pet.RES + self.category + "_" +  self.expression + ".png"
        )
        return list_