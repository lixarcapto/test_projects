

import tkinter as tk
from ..widget_composite.WidgetComposite \
    import WidgetComposite
from ..label_label.LabelLabel import LabelLabel
from ..frame.Frame import Frame

class LabelBox(WidgetComposite):

    def __init__(self, window, 
             title:str,
            key_list:list[str]):
        super().__init__(window, False)
        self.label_list = []
        self.widget.config(bg = "white")
        self.set_title(title)
        self.create_label_list(key_list)
        self.draw_in_vertical()

    def set_content(self, CONTENT_LIST:str):
        for i in range(len(self.label_list)):
            if(i >= len(CONTENT_LIST)):
                break
            self.label_list[i].set_text(
                CONTENT_LIST[i]
            )

    def __clean_elements(self):
        for label in self.label_list:
            label.margin.grid_forget()
        self.label_list = []

    def create_label_list(self, KEY_LIST):
        self.__clean_elements()
        label = None
        for k in KEY_LIST:
            label = LabelLabel(
                self.widget, k)
            label.widget.config(
                bg = "#caecfc"
            )
            self.label_list.append(label)

    def draw_in_vertical(self):
        n = 0
        for label in self.label_list:
            label.margin.pack(
                anchor = "w",
                fill=tk.BOTH,
                expand = True
            )
            n += 1

