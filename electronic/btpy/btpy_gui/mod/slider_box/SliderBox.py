


import tkinter as tk
from ..frame.Frame import Frame
from ..widget_composite.WidgetComposite import WidgetComposite
from ....btpy_checkers.mod.is_index.is_index import*
from ..input_slider.InputSlider import InputSlider

class SliderBox(WidgetComposite):

    """
    Checkbox type graphic component 
    that is used to ask the user to 
    enter multiple options from a list 
    by pressing click buttons.
    """

    def __init__(self, window, 
            is_horizontal:bool,
            TITLE:str = ""):
        super().__init__(
            window,
            is_horizontal
        )
        self.__text_list:list[str] = []
        self.__key_list:list[str] = []
        self.__widget_list = []
        self.set_title(TITLE)
    
    # PUBLIC -----------------------------

    def set_components(self, 
            KEY_LIST, RANGE):
        widget = None 
        self.__key_list = KEY_LIST
        self.__widget_list = []
        for i in range(len(KEY_LIST)):
            widget = InputSlider(
                self.widget,
                True,
                ""
            )
            widget.set_range(RANGE)
            self.__widget_list.append(
                widget
            )
        self.set_columns(1)
        self.set_content(KEY_LIST)

    def set_columns(self, COLUMNS):
        leng = len(self.__widget_list)
        x = 0
        y = 0
        for i in range(leng):
            self.__widget_list[i]\
                .grid(x, y, "w")
            x += 1
            if(x >= COLUMNS):
                x = 0
                y += 1

    def set_content(self, TEXT_LIST):
        widget:InputSlider = None 
        self.__text_list = TEXT_LIST
        i = 0
        for widget in self.__widget_list:
            widget.set_title(
                TEXT_LIST[i]
            )
            i += 1

    def set_range_for_all(self, 
            RANGE_LIST:list):
        widget:InputSlider = None
        for widget in self.__widget_list:
            widget.set_range(RANGE_LIST)
        
    def set_value_for_all(self, VALUE):
        widget:InputSlider = None 
        for widget in self.__widget_list:
            widget.set_value(VALUE)

    def set_value(self, DICT:dict):
        idx = 0
        for k in DICT:
            idx = self.__key_list.index(k)
            self.__widget_list[idx]\
                .set_value(DICT[k])

    def get_value(self)->dict:
        dict_ = {}
        leng = len(self.__widget_list)
        v = None
        k = ""
        for i in range(leng):
            v = self.__widget_list[i]\
                .get_value()
            k = self.__key_list[i]
            dict_[k] = v
        return dict_
        