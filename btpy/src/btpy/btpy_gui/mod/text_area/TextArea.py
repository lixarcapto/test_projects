
import tkinter as tk
from ..widget_composite.WidgetComposite import WidgetComposite

class TextArea(WidgetComposite):

    def __init__(self, window, 
            title:str = ""):
        super().__init__(window)
        self.text_area = None
        self.scroll_bar = None
        self.is_enabled:bool = False
        self.__init_components()
        self.set_title(title)
        
    def __init_components(self):
        self.text_area = tk.Text(
            self.widget)
        self.scroll_bar =  tk.Scrollbar(
            self.widget)
        # dibujar -------------------------
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
        
    def set_is_enabled(self, BOOL:bool):
        self.is_enabled = BOOL
        self.text_area.config(
            state = tk.DISABLED)
        
    def __set_text(self, TEXT):
        self.text_area.delete(
                "1.0", tk.END)  
        # Borra todo el texto
        self.text_area.insert(
                "1.0", TEXT)

    def set_value(self, TEXT:str):
        if(self.is_enabled):
            self.__set_text(TEXT)
        else:
            self.text_area.config(
                state = tk.NORMAL)
            self.__set_text(TEXT)
            self.text_area.config(
                state = tk.DISABLED)

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
