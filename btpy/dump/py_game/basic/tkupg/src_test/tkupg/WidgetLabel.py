


from .WidgetElementText import WidgetElementText
import tkinter as tk
from PIL import ImageTk

class WidgetLabel(WidgetElementText):

    def __init__(self, window_tk):
        self.widget = tk.Label(
            window_tk.widget)
        super().default_config()

    def set_text(self, string):
        self.widget.config(text=string)

    def add_text(self, new_text):
        text = self.widget.cget("text")
        text += new_text
        self.widget.config(text=text)

    def get_text(self):
        return self.widget.cget("text")

    def extract_text(self):
        text = self.widget.cget("text")
        self.widget.config(text="")
        return text
