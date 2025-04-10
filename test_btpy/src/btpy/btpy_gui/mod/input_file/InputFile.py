
import tkinter as tk
from ..widget_composite.WidgetComposite import WidgetComposite
from ..frame.Frame import Frame
from tkinter import ttk
from ....btpy_gui.mod.text_field.TextField import TextField
from tkinter import filedialog

class InputFile(WidgetComposite):

    def __init__(self, window, title:str):
        super().__init__(window)
        self.button_load = None
        self.text_field = None
        self.__init_components()
        self.set_title(title)

    def __init_components(self):
        self.button_load = tk.Button(
            self.widget, 
            text = "search"
        )
        self.text_field = TextField(
            self.widget
        )
        # dibujar ------------------------
        self.button_load.grid(
            row = 0, column= 0
        )
        self.text_field.widget.grid(
            row = 0, column= 1
        )

    def search_folder(self):
        def fn():
            path = filedialog.askdirectory()
            self.text_field\
                .set_character_width(
                    len(path))
            self.text_field.set_value(
                path)
        self.button_load.config(
            command = fn)
        
    def search_file(self):
        def fn():
            path = filedialog\
                .askopenfilename()
            self.text_field\
                .set_character_width(
                    len(path))
            self.text_field.set_value(
                path)
        self.button_load.config(
            command = fn)

    def get_value(self)->str:
        return self.text_field.get_value()
    
    def set_value(self, TEXT:str):
        self.text_field.set_value(TEXT)