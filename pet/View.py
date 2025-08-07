

from btpy.Btpy import Btpy
from Model import Model

class View:

    def __init__(self):
        print("init")
        self.time = Btpy.Time(0, 0, 0, 0)
        print(self.time.get_actual_hour())
        self.model = Model()
        self.window = Btpy.Window("titulo")
        self.button = Btpy.Button(
            self.window, "give food")
        self.button.pack()
        self.button_offend = Btpy.Button(
            self.window, "offend")
        self.button_offend.pack()
        self.label = Btpy.Canvas(self.window, "PJ")
        self.label.pack()
        self.label.set_size(400, 400)
        def fn(e):
            self.model.feed()
            self.update()
        self.button.add_listener(fn)
        def fn(e):
            self.model.offend()
            self.update()
        self.button_offend.add_listener(fn)
        self.update()
        self.window.start()

    def update(self):
        self.label.repaint()
        self.label.draw_image_layers(
            [0, 0],
            self.model.pet.get_path_list(),
            0
        )