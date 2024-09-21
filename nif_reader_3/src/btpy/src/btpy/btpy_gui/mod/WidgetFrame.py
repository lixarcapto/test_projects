


from .WidgetElement import WidgetElement
import tkinter

class WidgetFrame(WidgetElement):

    def __init__(self, widget):
        super().__init__()
        self.widget = tkinter.Frame(
            widget)