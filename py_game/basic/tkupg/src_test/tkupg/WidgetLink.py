

from .WidgetElementText import WidgetElementText
import tkinter as tk
import webbrowser

class WidgetLink(WidgetElementText):

    def __init__(self, window_tk, url):
        self.widget = tk.Button(
            window_tk.widget)
        super().default_config()
        self.url = url
        self.set_text(self.url)
        self.set_font("Arial", 12, "italic")
        self.set_foreground("blue")
        self.add_listener(self.__open_browser)

    def set_text(self, string):
        self.widget.config(text=string)

    def add_listener(self, function):
        self.widget.config(command=function)

    def __open_browser(self):
        # Open the URL in the default web 
        # browser
        webbrowser.open(self.url)
