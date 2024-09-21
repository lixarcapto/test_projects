

from .WidgetButton import WidgetButton
import tkinter as tk
import webbrowser

class WidgetLink(WidgetButton):

    def __init__(self, widget, url):
        self.widget = tk.Button(
            widget)
        super().default_config()
        self.url = url
        self.set_text(self.url)
        self.set_font("Arial", 12, "italic")
        self.set_foreground("blue")
        self.add_listener(self.__open_browser)

    def add_listener(self, function):
        self.widget.config(command=function)

    def __open_browser(self):
        # Open the URL in the default web 
        # browser
        webbrowser.open(self.url)
