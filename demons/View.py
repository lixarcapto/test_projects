

from btpy.Btpy import Btpy
from Model import Model

class View:

    def __init__(self):
        self.model = Model()
        self.window = Btpy.Window(
            ""
        )
        self.canvas = Btpy.Canvas(
            self.window.widget,
            "Demon"
        )
        self.canvas.grid(0, 0)
        self.canvas.set_size(400, 400)
        self.image_swiper = Btpy\
            .SwiperImage(
                self.window.widget,
                "symbol"
        )
        self.image_swiper.grid(0, 1)
        path_list = self.model\
            .get_symbol_paths()
        self.image_swiper.set_content(
            path_list
        )
        self.candle_box = Btpy\
            .SwitchImageBox(
                self.window.widget
            )
        self.candle_box.grid(0, 2)
        self.candle_box.set_components(3)
        self.candle_box.set_seleted_image_path(
            "./res/candle_on.png"
        )
        self.candle_box.set_unseleted_image_path(
            "./res/candle_off.png"
        )
        self.button_call = Btpy.Button(
            self.window.widget, "call"
        )
        self.button_call.grid(1, 1)
        self.button_call.add_listener(
            self.update
        )
        self.window.start()

    def update(self):
        self.canvas.repaint()
        self.model.candle_list = self\
            .candle_box.get_values()
        idx = self.image_swiper\
            .get_index()
        self.model.symbol_selected = idx
        self.model.create_demon()
        dict_ = self.model.render_dict()
        self.canvas.draw_path_image(
            [0, 0],
            dict_["PATH"]
        )