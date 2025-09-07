


import tkinter as tk
from ..frame.Frame import Frame
from ..widget_composite.WidgetComposite import WidgetComposite
from ..button_symbol.ButtonSymbol import ButtonSymbol

class ChipInput(WidgetComposite):

    def __init__(self, window, title:str,
            key_list:list[str]):
        super().__init__(window)
        self.__frame_selector = None
        self.__label = None
        self.__frame_inventory = None
        self.__button_list = []
        self.__key_list = []
        self.__key_selected = []
        self.__text_list = []
        self.__button_item_dict = {}
        self.__button_inventory = []
        self.__init_components(window)
        self.set_title(title)
        self.__create_button_list(key_list)

    def __init_components(self, window):
        self.__frame_selector = tk.Frame(
            self.widget,
            borderwidth = 1,
            relief = "solid"
        )
        self.__label = tk.Label(
            self.widget, 
            text = "Inventory",
            borderwidth = 1,
            relief = "solid",
            font = self.default_font
        )
        self.__frame_inventory = tk.Frame(
            self.widget
        )
        # dibujar -------------------------
        self.__frame_selector.pack()
        self.__label.pack(
            expand=True, fill=tk.BOTH)
        self.__frame_inventory.pack()

    def set_font_color(self, COLOR):
        super().set_font_color(COLOR)
        self.__label.config(fg = COLOR)
        for button in self.__button_inventory:
            button.config(fg = COLOR)
        for button in self.__button_list:
            button.config(fg = COLOR)

    def set_background_color(self, COLOR):
        super().set_background_color(
            COLOR)
        self.__label.config(bg = COLOR)
        self.__frame_inventory.config(
            bg = COLOR)
        self.__frame_selector.config(
            bg = COLOR)
        for button in self.__button_inventory:
            button.config(bg = COLOR)
        for button in self.__button_list:
            button.config(bg = COLOR)
    
    def get_value(self):
        return self.__key_selected
    
    def set_value(self, KEY_LIST:str):
        self.__format_button_items()
        text = ""
        i = 0
        self.__key_selected = KEY_LIST
        for k in KEY_LIST:
            self.__create_button_item(
                k, self.__text_list[i]
            )
            i += 1
    
    def set_content(self, TEXT_LIST:str):
        button:tk.Button = None
        i = 0
        self.__text_list = TEXT_LIST
        for button in self.__button_list:
            button.config(
                text = TEXT_LIST[i]
            )
            i += 1

    def set_components(self, 
            KEY_LIST:list[str]):
        self.__text_list = KEY_LIST
        self.__key_list = KEY_LIST
        self.__format_button_list()
        self.__create_button_list(
            KEY_LIST
        )

    # ----------------------------------
    # PRIVATE

    def __is_selected(self, key):
        if(key in self.__key_selected):
            return True
        return False

    def __format_button_items(self):
        key_list = []
        for k in self.__button_item_dict:
            self.__button_item_dict[k]\
                .pack_forget()
            key_list.append(k)
        for k in key_list:
            del(self.__button_item_dict[k])
            
    def __format_button_list(self):
        for button in self.__button_list:
             button.pack_forget()
        self.__button_list = []
        self.__format_button_items()

    def __create_button_selector(self, 
            KEY:str):
        button = tk.Button(
            self.__frame_selector, 
            text = KEY,
            bg = self.__label.cget("bg"),
            fg = self.__label.cget("fg"),
            font = self.default_font
        )
        button.pack(side=tk.LEFT)
        def aux(key):
            def fn():
                if(self.__is_selected(
                        key)):
                    return None
                self.__key_selected\
                    .append(key)
                idx = self.__key_list\
                    .index(key)
                text = self\
                    .__text_list[idx]
                self.__create_button_item(
                    key, text
                )
            return fn
        button.config(
            command = aux(KEY)
        )
        self.__button_list.append(button)

    def __create_button_list(
            self, key_list
        ):
        for key in key_list:
            self.__create_button_selector(
                key
            )

    def __create_button_item(self, 
            key, text):
        button = ButtonSymbol(
            self.__frame_inventory,
            text,
            "x"
        )
        def fn(e):
            self.__destroy_button(key)
            idx = self.__key_selected\
                .index(key)
            del(self.__key_selected[idx])
        button.add_listener(fn)
        button.margin.pack(anchor="w")
        self.__button_item_dict\
            [key] = button
        
    def __destroy_button(self, key):
        n = 0
        button = self.__button_item_dict\
            [key]
        button.margin.pack_forget()
        del(self.__button_item_dict\
            [key]
        )


            



