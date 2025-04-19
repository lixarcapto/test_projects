
import tkinter as tk
from ..widget_standard.WidgetStandard import WidgetStandard
from ..on_focus_widget.OnFocusWidget import OnFocusWidget

class SwitchRadio(OnFocusWidget):

    def __init__(self, window, 
            variable_, 
            number, 
            text = ""):
        super().__init__(window)
        self.is_selected = tk.BooleanVar()
        self.widget = tk.Radiobutton(
            self.margin, 
            text = text, 
            variable= variable_,
            value = number,
            borderwidth = 1,
            relief= "solid",
            anchor="w"
        )
        self.add_widget(self.widget)
        self.add_default_listener()

    def add_on_change_listener(self, 
            CALLBACK):
        """
            Es una callback sin argumento
        """
        self.widget.config(
            command = CALLBACK)