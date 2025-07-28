


import tkinter as tk
from ..frame.Frame import Frame
from ..widget_composite.WidgetComposite import WidgetComposite
from ..switch_check.SwitchCheck import SwitchCheck
from ....btpy_checkers.mod.is_index.is_index import*

class CheckBox(WidgetComposite):

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
        self.__button_list:SwitchCheck = []
        self.set_title(TITLE)
    
    # PUBLIC -----------------------------

    def get_value(self)->list[int]:
        """
        Function that gets a list 
        of the indices of the currently 
        checked buttons.
        """
        key_list = []
        n = 0
        for button in self.__button_list:
            if(button.get_value()):
                key_list.append(n)
            n += 1
        return key_list
    
    def set_value(self, INDEX:int)->None:
        if(not is_index(INDEX, 
                self.__button_list)):
            raise Exception(
            "The INDEX parameter is " \
            + f"not a valid index.({INDEX})"
            )
        """
        function that marks the button 
        with the index indicated in 
        the INDEX parameter.
        """
        n = 0
        for button in self.__button_list:
            if(INDEX == n):
                button.set_value(True)
            else:
                button.set_value(False)
            n += 1
    
    def add_on_change_listener(self, 
            CALLBACK_ARGSX0:callable)->None:
        """
        Funcion que activa la callback
        cuando el listener detecta 
        los eventos on_change sobre
        los botones SwitchCheck.
        La callback recibe cero argumentos,
        por eso su nombre X0.
        """
        leng = self.__button_list
        for i in self.__button_list:
            self.__button_list[i]\
                .add_on_change_listener(
                    CALLBACK_ARGSX0
                )
            
    def set_content(self, 
            TEXT_LIST:list[str])->None:
        """
        Function that draws a list of 
        texts on each button according 
        to the order of their indices.
        """
        self.__format_button()
        self.__create_button_list(TEXT_LIST)
            
    # ------------------------------------

    # PRIVATE ----------------------------

    def __format_button(self):
        button:SwitchCheck = None
        for button in self.__button_list:
            button.pack_forget()
        self.__button_list = []

    def __create_button_list(self, 
                TITLE_LIST:str):
        leng = len(TITLE_LIST)
        button = None
        for i in range(leng):
            button = SwitchCheck(
                self.widget, TITLE_LIST[i]
            )
            self.__button_list.append(
                button)
            button.pack(True)
        