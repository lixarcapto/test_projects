

import tkinter as tk
from ..widget_standard.WidgetStandard import WidgetStandard
from ..create_photo_image.create_photo_image import*
from tkinter import font
from ..button.Button import Button

class SimpleCard(WidgetStandard):

    """
    Esta es una carta simple generica
    que sirve tanto para button card
    como label card. 
    __init__(
        widget, 
        key_order:str,
        has_button:bool
    )
    Estilos:
    * vertical
    * vertical_invert
    * horizontal
    * horizontal_invert

    TODO: mejorar para que no desperdicie
    memoria en widgets que no se usan.
    """

    def __init__(self, window,
                 key_order:str,
                 has_button:bool):
        """
        * vertical
        * vertical_invert
        * horizontal
        * horizontal_invert
        """
        super().__init__(window)
        self.widget = tk.Frame(
            self.margin
        )
        TITLE = "no title"
        self.widget.pack(
            padx=1, pady=1,
            expand=True, fill=tk.BOTH
        )
        self.buffer_image = None
        self.label_icon = tk.Label(
            self.widget,
            bg = "black"
        )
        self.has_button:bool = has_button
        self.button_click = None
        self.label_title = None
        self.label_description = None
        if(key_order == "vertical"):
            self.__draw_vertical(TITLE)
            self.__grid_vertical_normal()
        elif(key_order == "vertical_invert"):
            self.__draw_vertical(TITLE)
            self.__grid_vertical_invert()
        elif(key_order == "horizontal"):
            self.__draw_horizontal(TITLE)
            self.__grid_horizontal_normal()
        elif(key_order == "horizontal_invert"):
            self.__draw_horizontal(TITLE)
            self.__grid_horizontal_invert()
        self.set_margin_color("black")

    def __init_button(self, widget):
        self.has_button:bool = True
        self.button_click = Button(
            widget, "click here"
        )
        self.button_click\
            .set_background_color("green")
        self.button_click\
            .set_font_color("white")

    def __draw_horizontal(self, TITLE):
        font_ = font.Font(
            size=14, weight="bold")
        self.frame_title = tk.Frame(
            self.widget
        )
        self.label_title = tk.Label(
            self.frame_title, 
            font = font_,
            text = TITLE,
            anchor="w",
            bg = "gray"
        )
        self.label_description = tk.Label(
            self.frame_title,
            anchor="w"
        )
        # --------------------------------
        self.label_title.grid(
            row=0, column=0, sticky="nsew"
        )
        self.label_description.grid(
            row=1, column=0, sticky="nsew"
        )
        if(self.has_button):
            self.__init_button(
                self.frame_title)
            self.button_click.draw_in_grid(
                2, 0
            )
        # dibujado ----------------------

    def __grid_horizontal_normal(self):
        self.label_icon.grid(
            row=0, column=0, sticky="nsew"
        )
        self.frame_title.grid(
            row=0, column=1, sticky="nsew"
        )

    def __grid_horizontal_invert(self):
        self.frame_title.grid(
            row=0, column=0, sticky="nsew"
        )
        self.label_icon.grid(
            row=0, column=1, sticky="nsew"
        )

    def __draw_vertical(self, TITLE):
        font_ = font.Font(
            size=14, weight="bold")
        self.label_title = tk.Label(
            self.widget, 
            font = font_,
            text = TITLE,
            anchor="w",
            bg = "gray"
        )
        self.label_description = tk.Label(
            self.widget,
            anchor="w"
        )
        # --------------------------------
        
    def __grid_vertical_normal(self):
        self.label_title.grid(
            row=0, column=0, sticky="nsew"
        )
        self.label_icon.grid(
            row=1, column=0, sticky="nsew"
        )
        self.label_description.grid(
            row=2, column=0, sticky="nsew"
        )
        if(self.has_button):
            self.__init_button(
                self.widget)
            self.button_click.draw_in_grid(
                3, 0
            )

    def __grid_vertical_invert(self):
        
        self.label_icon.grid(
            row=0, column=0, sticky="nsew"
        )
        self.label_title.grid(
            row=1, column=0, sticky="nsew"
        )
        self.label_description.grid(
            row=2, column=0, sticky="nsew"
        )
        if(self.has_button):
            self.__init_button(
                self.widget)
            self.button_click.draw_in_grid(
                3, 0
            )

    def set_button_text(self, TEXT:str):
        self.button_click.set_title(TEXT)

    def set_title(self, TEXT:str):
        self.label_title.config(
            text = TEXT)

    def set_description(self, TEXT:str):
        self.label_description.config(
            text = TEXT)
        
    def add_listener(self, CALLBACK):
        if(self.has_button):
            self.button_click\
                .add_listener(CALLBACK)

    def set_icon(self, PATH:str, 
            size_list:list[int] = []):
        image_tk = None
        if(size_list == []):
            image_tk = create_photo_image(
                PATH)
        else:
            image_tk = create_photo_image(
                PATH, 
                size_list
            )
        self.buffer_image = image_tk
        self.label_icon.config(
            image = self.buffer_image)

