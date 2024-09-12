


from .WidgetElementText import WidgetElementText
import tkinter as tk

class WidgetInput(WidgetElementText):

    def __init__(self, window_tk):
        self.widget = tk\
            .Text(window_tk.widget)
        super().default_config()

    def reset_index(self):
        self.widget.mark_set("insert", 1.0)
        self.widget.see("insert")

    def set_text(self, text):
        self.widget.delete("1.0", tk.END)
        self.widget.insert("1.0", text)

    def add_text(self, text):
        self.widget.insert(tk.END, text)

    def get_text(self):
        return self.widget.get("1.0", tk.END)

    def extract_text(self):
        text = self.widget.get("1.0", tk.END)
        self.widget.delete("1.0", tk.END)
        return text
    
    def add_enter_listener(self, function):
        self.widget.bind("<Return>", function)
