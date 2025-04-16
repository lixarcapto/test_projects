


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
        self.width_text = 100
        self.widget.config(bg = "white")
        font_ = font.Font(
            family="Arial", 
            size=24, 
            weight="bold"
        )
        self.label_title_article = tk\
            .Label(
                self.widget,
                font = font_
            )
        font_ = font.Font(
            family="Arial", 
            size=16, 
            weight="bold"
        )
        self.subtitle = tk.Label(
            self.widget,
            font = font_,
            anchor="w"
        )
        font_ = font.Font(
            family="Arial", 
            size=12
        )
        self.content = tk.Label(
            self.widget,
            font = font_,
            anchor= "w"
        )
        self.label_title_article.grid(
            row = 0, column= 0
        )
        self.subtitle.grid(
            row = 1, column= 0, 
            sticky="w"
        )
        self.content.grid(
            row = 2, column= 0,
            sticky="nswe"
        )
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
        self.label_title_article\
            .config(text = TEXT)
        
    def set_title_article_color(self,
            COLOR):
        color = self.convert_to_tk_color(
            COLOR)
        self.label_title_article.config(
            fg = color)

    def set_subtitle(self, TEXT:str):
        self.subtitle.config(text = TEXT)

    def set_subtitle_color(self,
            COLOR):
        color = self.convert_to_tk_color(
            COLOR)
        self.subtitle.config(fg = color)

    def set_character_width(self, 
                CHAR_SIZE):
        self.width_text = CHAR_SIZE

    def set_content(self, TEXT:str):
        new_text = TEXT.replace("\n", " ")
        new_text = sort_text(
            new_text,
            self.width_text
        )
        self.content.config(
            text = new_text)
        
    def set_content_color(self,
            COLOR):
        color = self.convert_to_tk_color(
            COLOR)
        self.content.config(
            fg = color)