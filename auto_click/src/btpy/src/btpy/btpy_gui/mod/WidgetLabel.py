


from .WidgetTextual import WidgetTextual
import tkinter as tk
from PIL import ImageTk

class WidgetLabel(WidgetTextual):

    def __init__(self, window_tk):
        self.widget = tk.Label(
            window_tk.widget)
        super().default_config()
