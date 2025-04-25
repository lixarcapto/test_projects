


import tkinter as tk
from ..widget_composite.WidgetComposite \
    import WidgetComposite
from ..frame.Frame import Frame
from tkinter import font
from ....btpy_string.mod.sort_text.sort_text import*

class Article(WidgetComposite):

    def __init__(self, window, 
            title:str):
        super().__init__(
            window, 
            False
        )
        self.set_title(title)
        self.width_text = 50
        self.widget.config(bg = "white")
        font_ = font.Font(
            family="Arial", 
            size=24, 
            weight="bold"
        )
        self.label_title_article = tk.Text(
            self.widget,
            font = font_,
            state=tk.DISABLED,
            borderwidth = 0,
            height=1
        )
        font_ = font.Font(
            family="Arial", 
            size=16, 
            weight="bold"
        )
        self.subtitle = tk.Text(
            self.widget,
            font = font_,
            state=tk.DISABLED,
            borderwidth = 0,
            height=1
        )
        font_ = font.Font(
            family="Arial", 
            size=12
        )
        self.content = tk.Text(
            self.widget,
            font = font_,
            state=tk.DISABLED,
            borderwidth = 0
        )
        self.label_title_article.grid(
            row = 0, column= 0, 
            sticky="w",
            padx=(20, 2)
        )
        self.subtitle.grid(
            row = 1, column= 0, 
            sticky="w",
            padx=(20, 2)
        )
        self.content.grid(
            row = 2, column= 0,
            sticky="w",
            padx=(20, 2),
            pady=(20, 2)
        )
        self.set_character_width(
            self.width_text)
        self.set_background_color("white")
    
    def set_background_color(self, COLOR):
        color = self.convert_to_tk_color(
            COLOR)
        self.widget.config(
            bg = color)
        self.label_title_article.config(
            bg = color)
        self.subtitle.config(
            bg = color)
        self.content.config(
            bg = color)

    def set_title_article(self, TEXT:str):
        new_text = TEXT.replace("\n", " ")
        new_text = sort_text(
            new_text,
            self.width_text
        )
        self.label_title_article.config(
            state = tk.NORMAL)
        self.label_title_article.delete(
            "1.0", tk.END)  
        # Borra todo el texto
        self.label_title_article.insert(
            "1.0", new_text)  
        self.label_title_article.config(
            state = tk.DISABLED)
        
    def set_title_article_color(self,
            COLOR):
        color = self.convert_to_tk_color(
            COLOR)
        self.label_title_article.config(
            fg = color)

    def set_subtitle(self, TEXT:str):
        new_text = TEXT.replace("\n", " ")
        new_text = sort_text(
            new_text,
            self.width_text
        )
        self.subtitle.config(
            state = tk.NORMAL)
        self.subtitle.delete(
            "1.0", tk.END)  
        # Borra todo el texto
        self.subtitle.insert(
            "1.0", new_text)  
        self.subtitle.config(
            state = tk.DISABLED)

    def set_subtitle_color(self,
            COLOR):
        color = self.convert_to_tk_color(
            COLOR)
        self.subtitle.config(fg = color)

    def set_character_width(self, 
                CHAR_SIZE):
        self.width_text = CHAR_SIZE
        size = round(self.width_text / 2)
        self.label_title_article.config(
            width = size)
        size = round(self.width_text / 1.4)
        self.subtitle\
            .config(width = size)
        self.content\
            .config(width = CHAR_SIZE)

    def set_content(self, TEXT:str):
        new_text = TEXT.replace("\n", " ")
        new_text = sort_text(
            new_text,
            self.width_text
        )
        line_height = new_text.count("\n")
        self.content.config(
            height=line_height + 2)
        self.content.config(
            state = tk.NORMAL)
        self.content.delete(
            "1.0", tk.END)  
        # Borra todo el texto
        self.content.insert(
            "1.0", new_text)  
        self.content.config(
            state = tk.DISABLED)
        
    def set_content_color(self,
            COLOR):
        color = self.convert_to_tk_color(
            COLOR)
        self.content.config(
            fg = color)