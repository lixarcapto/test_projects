

from tkinter import ttk
import tkinter as tk
from ..widget_composite.WidgetComposite import WidgetComposite
from ..frame.Frame import Frame

class Combobox(WidgetComposite):

    """
    A combobox-type graphic component 
    that converts it to a drop-down 
    list. It allows the user to select 
    an option from a drop-down list.
    """

    def __init__(self, 
            window,
            IS_HORIZONTAL:bool,
            TITLE:str = ""):
        super().__init__(window, True)
        self.combobox = None  # public
        self.__text_list:list[str] = []
        self.__init_components(window)
        self.set_title(TITLE)
        
    def __init_components(self, window)\
            ->None:
        self.combobox = ttk.Combobox(
            self.widget,
            font = self.get_font()
        )
        self.combobox.grid(
            row=0, column=1, 
            sticky="nsew",
            padx=1, pady=(2, 1)
        )
        
    def add_change_listener(self, 
            CALLBACK_ARGS_X1:callable)\
            ->None:
        self.combobox.bind(
            "<<ComboboxSelected>>", 
            CALLBACK_ARGS_X1
        )
        
    def set_size(self, CHAR_SIZE:int)\
            ->None:
        self.combobox.config(
            width=CHAR_SIZE)
        
    def set_content(self, 
            TEXT_LIST:list[str])->None:
        """
        Function that assigns a list 
        of texts to display inside 
        the combobox widget's drop-down 
        box. By default, it will use 
        the text at index 0 of the 
        list as the initial value.
        """
        self.__text_list = TEXT_LIST
        self.combobox.config(
            values = TEXT_LIST)
        self.set_value(0)

    def get_value(self)->int:
        """
        Function that obtains the index 
        of the list text selected by 
        the user.
        """
        text = self.combobox.get()
        return self.__text_list.index(text)
    
    def set_value(self, INDEX:int)\
            ->None:
        """
        Function that assigns a 
        selected element by its index. 
        The index is the index of the 
        text list assigned with 
        set_content.
        """
        text = self.__text_list[INDEX]
        self.combobox.set(text)
        
