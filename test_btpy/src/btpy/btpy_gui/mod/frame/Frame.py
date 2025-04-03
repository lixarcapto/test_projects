

import tkinter as tk
from ..widget_standard.WidgetStandard import WidgetStandard

class Frame(WidgetStandard):

    def __init__(self, window):
        super().__init__()
        self.widget = tk.Frame(
            window.widget)