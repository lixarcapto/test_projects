

import tkinter as tk
from ..on_focus_widget.OnFocusWidget import OnFocusWidget

class Button(OnFocusWidget):

    """
    Este modulo crea un boton de texto
    que detecta eventos por click en su 
    area para ejecutar una funcion callback.
    """

    def __init__(self, window, 
            TITLE:str = ""):
        super().__init__(window)
        widget = tk.Button(
            self.margin
        )
        self.add_widget(widget)
        self.set_title(TITLE)
        self.set_background_color(
            [205, 205, 205]
        )
        self.widget.config(
            font = self.default_font)
        