


from btpy.src.btpy.Btpy import Btpy
import tkinter as tk
from .PlayerFrame import PlayerFrame

class View:

    def __init__(self) -> None:
        self.event_triggered = False
        self.is_on = False
        self.main_mode = "MAIN_MENU"
        self.on_buffer_route = ""
        self.player_frame = None
        self.init_calls()
        #self.text.widget.config(state=tk.DISABLED)
        
    def init_calls(self):
        self.init_window()
        self.player_frame = PlayerFrame(
            self.window)
        self.window.widget.update()

    def init_window(self):
        self.window = Btpy.Window()
        self.window.set_full_screen()

    def add_update_listener(self, function):
        self.player_frame.add_update_listener(
            function)

    def destroy(self):
        self.window.destroy()
        
    def receive(self, message:dict):
        self.player_frame.receive(message)

    def request(self)->dict:
        return self.player_frame.request()
        
    def start(self):
        self.window.start()