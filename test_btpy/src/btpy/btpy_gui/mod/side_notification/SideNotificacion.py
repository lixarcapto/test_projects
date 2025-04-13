

import tkinter as tk
from ..widget_standard.WidgetStandard import WidgetStandard
from ....btpy_utilitys.mod.repeat_each_async.repeat_each_async import*
from tkinter import font 

class SideNotificacion(WidgetStandard):

    def __init__(self, window):
        super().__init__(window)
        font_ = font.Font(
            size=12, weight="bold")
        self.widget = tk.Button(
            self.margin, 
            text=" > ",
            font = font_,
            bg = "gray",
            fg = "white"
        )
        self.content_label = tk.Label(
            self.margin, text = "",
            bg = "white"
        )
        self.flag = None
        self.is_waiting = False
        self.time_notificacion = 2
        self.widget.grid(
            row=0, column=0, 
            sticky="nswe",
            padx=(1, 0), pady=1
        )
        def fn():
            self.close()
        self.widget.config(command = fn)

    def set_title(self, TITLE):
        self.content_label.config(
            text = TITLE)

    def show(self, text):
        """
        Esta función se activará después 
        de 3 segundos.
        """
        if(self.is_waiting): return None
        self.is_waiting = True
        self.set_title(text)
        self.content_label.grid(
            row=0, column=1, 
            sticky="nswe", 
            padx=(0, 1), pady=1
        )
        def fn(n):
            self.close()
            return True
        self.flag = repeat_each_async(
            self.time_notificacion, fn
        )
        
    def close(self):
        self.content_label.grid_forget()
        self.is_waiting = False
        self.flag.set(False)