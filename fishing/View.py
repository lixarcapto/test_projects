

from btpy.Btpy import Btpy
from Model import Model

class View:

    def __init__(self):
        self.window = Btpy.Window("")
        self.model = Model()
        self.text = Btpy.TextArea(
            self.window, "fish")
        self.text.pack()
        self.text.set_size(30, 15)
        self.selector = Btpy.Combobox(
            self.window, True, "sea"
        )
        self.selector.pack()
        self.label_label = Btpy\
            .LabelLabel(
                self.window,
                " points "
            )
        self.label_label.set_font_size(14)
        self.label_label.pack()
        self.canvas = Btpy.Canvas(
            self.window, "canvas"
        )
        self.canvas.pack()
        self.canvas.set_size(500, 500)
        def fn(e):
            self.model.take_cane()
            self.update()
        self.canvas.add_right_click_listener(
            fn
        )
        def fn(n):
            self.model.take_bait()
            self.update()
        self.model.flag = Btpy.repeat_each_async(
            self.model.loop_time,
            fn
        )
        list_ = self.model.get_sea_keys()
        self.selector.set_content(
            list_
        )
        def fn(e):
            idx = self.selector.get_value()
            list_ = self.model.get_sea_keys()
            self.model.change_sea(
                list_[idx]
            )
            print("change sea")
        self.selector.add_change_listener(
            fn
        )
        self.window.start()

    def draw_render(self, RENDER_DICT):
        if(RENDER_DICT["FISH"] == ""):
            return None
        self.canvas.draw_path_image(
            [0, 0],
            "./res/" + RENDER_DICT["FISH"] + ".png",
            0,
            [500, 500]
        )
        self.text.set_value(
            RENDER_DICT["TEXT"]
        )
        self.label_label.set_content(
            RENDER_DICT["VALUE"]
        )

    def update(self):
        self.canvas.repaint()
        render = self.model.render()
        self.draw_render(
            render
        )
        