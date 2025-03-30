
import tkinter as tk
from ..widget_standard.WidgetStandard import WidgetStandard
from ..frame.Frame import Frame
from tkinter import ttk
from ....btpy_gui.mod.text_field.TextField import TextField
from tkinter import filedialog

class InputFile(WidgetStandard):

    def __init__(self, window, title:str):
        super().__init__()
        self.widget = Frame(window)
        self.widget.set_border(1)
        self.label_title = tk.Label(
            self.widget.widget
        )
        self.button_load = tk.Button(
            self.widget.widget, 
            text = "search"
        )
        self.text_field = TextField(
            self.widget
        )
        self.set_title(title)

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

    def set_title(self, TEXT:str):
        self.label_title.config(text = TEXT)

    def get_title(self)->str:
        return self.label_title.cget("text")

    def pack(self, MARGIN:int = 0):
        self.widget.pack(MARGIN)
        self.label_title.grid(
            row = 0, column= 0
        )
        self.button_load.grid(
            row = 0, column= 1
        )
        self.text_field.widget.grid(
            row = 0, column= 2
        )