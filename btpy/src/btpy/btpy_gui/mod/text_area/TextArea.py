
import tkinter as tk
from ..widget_standard.WidgetStandard import WidgetStandard

class TextArea(WidgetStandard):

    def __init__(self, window):
        super().__init__()
        self.widget = tk.Frame(
            window.widget)
        self.text_area = tk.Text(
            self.widget)
        self.scroll_bar =  tk.Scrollbar(
            self.widget)
        self.__init_scroll_bar()
        
    def __init_scroll_bar(self):
        self.scroll_bar.config(
            command=self.text_area.yview)
        self.text_area.config(
            yscrollcommand
                =self.scroll_bar.set)
        self.text_area.grid(row=0, column=0, sticky="nsew")
        self.scroll_bar.grid(row=0, column=1, sticky="ns")
        self.widget.grid_rowconfigure(0, weight=1)
        self.widget.grid_columnconfigure(0, weight=1)
        
    def pack(self):
        self.widget.pack()

    def set_text(self, TEXT:str):
        self.text_area.insert(tk.END, TEXT)

    def get_text(self)->str:
        return  self.text_area.get(
            "1.0", tk.END)
    
    def set_character_width(self, 
            CHAR_NUMBER:int):
        self.text_area.config(
            width = CHAR_NUMBER)
        
    def set_character_height(self, 
            CHAR_NUMBER:int):
        self.text_area.config(
            height = CHAR_NUMBER)
