


import tkinter as tk
from ..widget_standard.WidgetStandard import WidgetStandard
from ..frame.Frame import Frame

class ButtonInventory(WidgetStandard):

    def __init__(self, window, title:str,
            key_list:list[str]):
        super().__init__()
        self.widget = None
        self.label_title = None
        self.frame_selector = None
        self.label = None
        self.frame_inventory = None
        self.__button_list = []
        self.__button_inventory = []
        self.__init_components(window)
        self.set_title(title)
        self.create_button_list(key_list)

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

    def create_button_list(self, key_list):
        button = None
        for key in key_list:
            button = tk.Button(
                self.frame_selector.widget, 
                text = key)
            button.pack(side=tk.LEFT)
            def aux(key):
                def fn():
                    if(self.is_selected(
                            key)):
                        return None
                    self.create_button(key)
                return fn
            button.config(
                command = aux(key))
            self.__button_list.append(
                button)

    def create_button(self, key):
        button = tk.Button(
            self.frame_inventory.widget, 
            text = key)
        def fn():
            self.destroy_button(key)
        button.config(command = fn)
        button.pack(side=tk.LEFT)
        self.__button_inventory.append(
            button)
        
    def destroy_button(self, key):
        n = 0
        for button in self.__button_inventory:
            if(key == button.cget("text")):
                self.__button_inventory[n]\
                    .destroy()
                del(self.__button_inventory[n])
            n += 1
        return False
    
    def __init_components(self, window):
        self.widget = Frame(
            window
        )
        self.widget.widget.config(
            borderwidth=1,
            relief = "solid"
        )
        self.label_title = tk.Label(
            self.widget.widget
        )
        self.frame_selector = Frame(
            self.widget)
        self.label = tk.Label(
            self.widget.widget, 
            text = "Inventory"
        )
        self.frame_inventory = Frame(
            self.widget
        )
        # dibujar -------------------------
        self.label_title.pack()
        self.frame_selector.pack()
        self.label.pack()
        self.frame_inventory.pack()

            



