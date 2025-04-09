

import tkinter as tk
from ..widget_composite.WidgetComposite \
    import WidgetComposite
from ..frame.Frame import Frame

class LabelColor(WidgetComposite):

    def __init__(self, window, title,
            color = ""):
        super().__init__(window, True)
        self.label_color = None
        self.__init_components()
        self.set_title(title)
        self.set_label_color(color)

    def __init_components(self):
        # dibujar componentes
        self.label_color = tk.Label(
            self.widget
        )
        self.label_color.config(
            text = "     "
        )
        self.label_color.grid(
            row = 0, column = 1,
            padx= 2, pady= 2
        )
        
    def set_label_color(self, color):
        self.label_color.config(
            bg = color,
            borderwidth=1,
            relief = "solid"
        )