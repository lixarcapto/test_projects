
import tkinter as tk
from ..widget_standard.WidgetStandard import WidgetStandard

class TextArea(WidgetStandard):

    def __init__(self, window, 
            title:str = ""):
        super().__init__()
        self.widget = tk.Frame(
            window.widget)
        self.label_title = tk.Label(
            self.widget)
        self.text_area = tk.Text(
            self.widget)
        self.scroll_bar =  tk.Scrollbar(
            self.widget)
        self.set_title(title)
        self.__init_components()

    def set_title(self, TEXT:str):
        self.label_title.config(
            text = TEXT)
        
    def __init_components(self):
        self.label_title.grid(
            row=0, column=0)
        self.scroll_bar.config(
            command=self.text_area.yview)
        self.text_area.config(
            yscrollcommand
                =self.scroll_bar.set)
        self.text_area.grid(
            row=1, column=0, sticky="nsew")
        self.scroll_bar.grid(
            row=1, column=1, sticky="ns")
        self.widget.grid_rowconfigure(
            0, weight=1)
        self.widget.grid_columnconfigure(
            0, weight=1)
        
    def pack(self):
        self.widget.pack()

    def set_value(self, TEXT:str):
        self.text_area.insert(tk.END, TEXT)

    def get_value(self)->str:
        return  self.text_area.get(
            "1.0", tk.END)
    
    def set_size(self, CHAR_WIDTH:int, 
            CHAR_HEIGHT:int):
        self.text_area.config(
            width = CHAR_WIDTH)
        self.text_area.config(
            height = CHAR_HEIGHT)
    
    def set_character_width(self, 
            CHAR_NUMBER:int):
        self.text_area.config(
            width = CHAR_NUMBER)
        
    def set_character_height(self, 
            CHAR_NUMBER:int):
        self.text_area.config(
            height = CHAR_NUMBER)
