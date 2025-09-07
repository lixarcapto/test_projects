
import tkinter as tk
import tkinter.font as tkFont

class TextArea:

    def __init__(self, widget, TEXT:str):
        self.widget = tk.Frame(
            widget,
            borderwidth=1,
            relief="solid" 
        )
        self.default_font = tkFont\
            .Font(
                family="Arial", 
                size=12
            )
        self.is_enabled:bool = True
        self.label_title = None
        self.text_area = None
        self.scroll_bar = None
        self.__init_label_title()
        self.__init_text_area()
        self.__init_scroll()
        self.set_title(TEXT)
        self.set_character_width(40)
        self.set_character_height(30)

    def __init_label_title(self):
        self.label_title = tk.Label(
            self.widget,
            anchor="w",
            font = self.default_font,
            borderwidth=1,
            relief="solid" 
        )
        self.label_title.grid(
            row=0, 
            column=0, 
            sticky="ew",
            ipadx=5,
            ipady=5
        )

    def __init_scroll(self):
        self.scroll_bar =  tk.Scrollbar(
            self.widget)
        self.scroll_bar.grid(
            row=1, column=1, sticky="ns")
        self.scroll_bar.config(
            command=self.text_area.yview)
        self.text_area.config(
            yscrollcommand=self.scroll_bar.set
        )

    def __init_text_area(self):
        self.text_area = tk.Text(
            self.widget,
            font= self.default_font
        )
        self.text_area.grid(
            row=1, 
            column=0, 
            sticky="nsew"
        )
        
    def set_title(self, TEXT:str):
        self.label_title.config(
            text = TEXT
        )

    def get_title(self):
        return self.label_title\
            .cget("text")

    def set_is_enabled(self, BOOL:bool):
        self.is_enabled = BOOL
        if(not self.is_enabled):
            self.text_area.config(
                state = tk.DISABLED)
        else:
            self.text_area.config(
                state = tk.NORMAL)
            
    def __set_text(self, TEXT):
        self.text_area.delete(
                "1.0", tk.END)  
        # Borra todo el texto
        self.text_area.insert(
                "1.0", TEXT)
        
    def set_font_size(self, SIZE:int):
        self.default_font.config(
            size = SIZE
        )
        self.widget.config(
            font=self.default_font
        )
        self.text_area.config(
            font=self.default_font
        )
        self.label_title.config(
            font=self.default_font
        )

    def set_font_family(self, 
            FONT_FAMILY_KEY:str):
        self.default_font.config(
            family = FONT_FAMILY_KEY
        )
        self.widget.config(
            font=self.default_font
        )
        self.text_area.config(
            font=self.default_font
        )
        self.label_title.config(
            font=self.default_font
        )

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
        text = self.text_area.get(
            "1.0", tk.END)
        return remove_char(
            text, 
            len(text) -1
        )
    
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
        
    def grid(self, ROW, COLUMN, 
             STICKY = ""):
        self.widget.grid(
            row = ROW, column= COLUMN,
            sticky= STICKY
        )
    
    def place(self, 
            LOCATION_X:int, 
            LOCATION_Y:int):
        self.widget.place(
            x=LOCATION_X,
            y=LOCATION_Y
        )

def remove_char(string:str, index:int)\
        ->str:
    """
    Función que elimina un carácter 
    de un String por su índice
    """
    array = list(string)
    del(array[index])
    array = "".join(array)
    return array