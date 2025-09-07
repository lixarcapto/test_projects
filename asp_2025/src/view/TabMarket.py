

from btpy.Btpy import Btpy
import os

class TabMarket(Btpy.Frame):

    def __init__(self, window):
        super().__init__(window)
        self.texture_pack:str = ""
        self.model = None
        self.widget_list = []
        self.y_max = 20

    def update(self):
        dict_ = self.model.render_market()
        self.widget_list = []
        e = None
        x = 0
        y = 0
        for k in dict_:
            e = Btpy.LabelLabel(
                self.widget,
                f" {k} "
            )
            e.set_font_size(12)
            e.set_content(f" {dict_[k]} ")
            e.grid(x, y)
            self.widget_list.append(e)
            if(y >= self.y_max):
                y = 0
                x += 1
            y += 1