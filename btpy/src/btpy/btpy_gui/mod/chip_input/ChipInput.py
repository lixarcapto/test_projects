


import tkinter as tk
from ..frame.Frame import Frame
from ..widget_composite.WidgetComposite import WidgetComposite

class ChipInput(WidgetComposite):

    def __init__(self, window, title:str,
            key_list:list[str]):
        super().__init__(window)
        self.__frame_selector = None
        self.__label = None
        self.__frame_inventory = None
        self.__button_list = []
        self.__button_inventory = []
        self.__init_components(window)
        self.set_title(title)
        self.__create_button_list(key_list)

    def set_foreground_color(self, COLOR):
        super().set_foreground_color(COLOR)
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

    def is_selected(self, key):
        for button in self.__button_inventory:
            if(key == button.cget("text")):
                return True
        return False
    
    def get_value(self):
        key_list = []
        for button in self.__button_inventory:
            key_list.append(
                button.cget("text"))
        return key_list
    
    def __format_button_list(self):
        for button in self.__button_list:
             button.pack_forget()
        self.__button_list = []
        for button in self.__button_inventory:
            button.pack_forget()
        self.__button_inventory = []

    def set_content(self, 
            KEY_LIST:list[str]):
        self.__format_button_list()
        self.__create_button_list(KEY_LIST)

    def __create_button_list(self, key_list):
        button = None
        for key in key_list:
            button = tk.Button(
                self.__frame_selector, 
                text = key,
                bg = self.__label.cget("bg"),
                fg = self.__label.cget("fg")
            )
            button.pack(side=tk.LEFT)
            def aux(key):
                def fn():
                    if(self.is_selected(
                            key)):
                        return None
                    self.__create_button(key)
                return fn
            button.config(
                command = aux(key))
            self.__button_list.append(
                button)

    def __create_button(self, key):
        button = tk.Button(
            self.__frame_inventory, 
            text = key,
            borderwidth = 1,
            relief = "solid",
            bg = self.__label.cget("bg"),
            fg = self.__label.cget("fg")
        )
        def fn():
            self.__destroy_button(key)
        button.config(command = fn)
        button.pack(side=tk.LEFT)
        self.__button_inventory.append(
            button)
        
    def __destroy_button(self, key):
        n = 0
        for button in self.__button_inventory:
            if(key == button.cget("text")):
                self.__button_inventory[n]\
                    .destroy()
                del(self.__button_inventory[n])
            n += 1
        return False
    
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
            relief = "solid"
        )
        self.__frame_inventory = tk.Frame(
            self.widget
        )
        # dibujar -------------------------
        self.__frame_selector.pack()
        self.__label.pack(
            expand=True, fill=tk.BOTH)
        self.__frame_inventory.pack()

            



