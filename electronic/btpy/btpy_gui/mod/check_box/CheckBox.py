


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
        self.__text_list:list[str] = []
        self.__key_list:list[str] = []
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
        key:str = ""
        for button in self.__button_list:
            key = self.__key_list[n]
            if(button.get_value()):
                key_list.append(key)
            n += 1
        return key_list
    
    def set_value(self, 
            KEY_LIST:list[str])\
            ->None:
        # ------------------------------
        # convertir todos a false
        leng = len(self.__button_list)
        for i in range(leng):
            self.__button_list\
                .set_value(False)
        # ---------------------------
        # detectar los indices de cada
        # widget a seleccionar
        idx_list = []
        idx = 0
        for e in self.__key_list:
            idx = KEY_LIST.index(e)
            idx_list.append(idx)
        # -----------------------------
        # aplicar el estado seleccionado
        # a cada widget designado
        for idx in idx_list:
            self.__button_list[idx]\
                .set_value(True)
    
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
            
    def set_components(self, 
            KEY_LIST:list[str])->None:
        """
        Function that creates components 
        by assigning them the keys 
        sent as identifiers
        """
        self.__key_list = KEY_LIST
        self.__format_button()
        self.__create_button_list(
            len(KEY_LIST))
        self.set_columns(1)

    def set_content(self, 
            TEXT_LIST:list[str]):
        """
        function that draws a list 
        of texts for the components
        """
        self.__set_text_list(TEXT_LIST)
            
    # ------------------------------------

    # PRIVATE ----------------------------

    def __format_button(self):
        button:SwitchCheck = None
        for button in self.__button_list:
            button.pack_forget()
        self.__button_list = []

    def __set_text_list(self, TEXT_LIST:list[str]):
        leng = len(self.__button_list)
        self.__text_list = TEXT_LIST
        for i in range(leng):
            self.__button_list[i]\
                .set_content(TEXT_LIST[i])

    def set_columns(self, COLUMNS):
        leng = len(self.__button_list)
        x = 0
        y = 0
        for i in range(leng):
            self.__button_list[i]\
                .draw_in_grid(y, x, "EW")
            x += 1
            if(x >= COLUMNS):
                x = 0
                y += 1

    def __create_button_list(self, SIZE):
        button = None
        for i in range(SIZE):
            button = SwitchCheck(
                self.widget, ""
            )
            self.__button_list.append(
                button)
        