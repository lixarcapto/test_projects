


import tkinter as tk
from ..widget_composite.WidgetComposite \
    import WidgetComposite
from ..frame.Frame import Frame
import tkinter.font as font

class LabelLabel(WidgetComposite):

    def __init__(self, window, title = ""):
        super().__init__(window, True)
        self.label_content = None
        self.__init_components()
        self.set_title(title)

    def set_text(self, TEXT:str):
        self.label_content.config(text = TEXT)

    def get_text(self)->str:
        return self.label_content.cget(
            "text")
    
    def __init_components(self):
        self.label_content = tk.Label(
            self.widget)
        # Alinea a la izquierda
        self.label_content.pack(
            expand=True, fill=tk.BOTH
        )
        # Alinea a la derecha