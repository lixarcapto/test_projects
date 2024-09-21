


from .WidgetTextual import WidgetTextual
import tkinter as tk
from PIL import ImageTk

class WidgetLabel(WidgetTextual):

    def __init__(self, widget):
        self.widget = tk.Label(
            widget)
        super().default_config()
