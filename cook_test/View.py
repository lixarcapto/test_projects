

from btpy.Btpy import Btpy
from Persistence import Persistence
from Model import Model
from FrameMain import FrameMain

class View:

    def __init__(self):
        self.window = Btpy.WindowNav(
            "titulo")
        self.model = Model()
        self.frame_main = FrameMain(
            self.window.widget,
            self.model)
        self.frame_main.model = self.model
        self.window.add_frame(
            "main", self.frame_main
        )
        self.window\
            .set_on_change_callback(
                lambda :()
        )

    def start(self): 
        self.window.select_frame(
            "main")
        self.window.start()