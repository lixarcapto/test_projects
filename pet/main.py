

from btpy.Btpy import Btpy

class Pet:

    RES = "./res/"
    EXPRESION_RANGES = {
        "sad":[0, 5],
        "normal":[6, 10],
        "happy":[11, 15]
    }

    def __init__(self):
        self.category = "fish"
        self.color = "blue"
        self.expression = "normal"
        self.emotion_value = 0
        self.energy = 0
        self.update()

    def update(self):
        self.identify_emotion()

    def identify_emotion(self):
        self.expression = Btpy.whats_range(
            Pet.EXPRESION_RANGES,
            self.emotion_value
        )[0]
        if(self.energy == 0):
            self.expression = "sleep"

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
            Pet.RES + self.category + "_" + self.color + ".png"
        )
        list_.append(
            Pet.RES + self.category + "_" +  self.expression + ".png"
        )
        return list_

def main():
    print("init")
    time = Btpy.Time(0, 0, 0, 0)
    print(time.get_actual_hour())
    pet = Pet()
    window = Btpy.Window("titulo")
    button = Btpy.Button(
        window, "give food")
    button.pack()
    label = Btpy.Canvas(window, "PJ")
    label.pack()
    label.set_size(400, 400)
    def update():
        label.repaint()
        label.draw_image_layers(
            [0, 0],
            pet.get_path_list()
        )
    def fn(e):
        pet.feed()
        pet.update()
        update()
    update()
    button.add_listener(fn)
    window.start()

main()