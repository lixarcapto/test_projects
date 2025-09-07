

from model.Model import Model
from btpy.Btpy import Btpy
import tkinter as tk

class View:

    def __init__(self):
        self.model = Model()
        self.window = Btpy.Window(
            "NIF reader")
        self.window.set_size(1000, 700)
        self.frame_head = None
        self.title_nif = None
        self.size_range_input\
            = [150, 50]
        self.input_file = None
        self.button_read = None
        self.button_reset = None
        self.text_area = None
        # ------------------------------
        self.init_frame_head()
        self.init_text_area()
        
    def init_text_area(self):
        self.text_area = Btpy.TextArea(
            self.window.widget, 
            "Nif actual"
        )
        self.text_area.widget\
            .pack()
        self.text_area.set_size(
            self.size_range_input[0], 
            self.size_range_input[1]
        )

    def init_frame_head(self):
        self.frame_head = tk.Frame(
            self.window.widget
        )
        self.frame_head.pack()
        self.title_nif = Btpy.LabelImage(
            self.frame_head
        )
        self.title_nif.set_path_image(
            "./res/image/nif_icon.png")
        self.title_nif.grid(0, 0)
        self.input_file = Btpy.InputFile(
            self.frame_head, "text"
        )
        self.input_file.grid(0, 1)
        self.input_file.set_file_types(
            "TEXT"
        )
        self.button_read = Btpy.Button(
            self.frame_head)
        self.button_read.set_title("Read")
        self.button_read.grid(0, 2)
        self.button_reset = Btpy.Button(
            self.frame_head)
        self.button_reset.set_title("Reset")
        self.button_reset.grid(0, 3)
        def fn():
            self.load_and_start()
        self.button_read.add_listener(fn)
        def fn():
            self.start_nif()
        self.button_reset.add_listener(fn)
        self.add_window_listener()

    def load_and_start(self):
        v = self.input_file.get_value()
        self.model.request(
            "load_nif_file",
            {"path": v}
        )
        self.start_nif()
        self.update()

    def write_as_list(self, LIST, 
            SYMBOL = "). "):
        txt = ""
        n = 1
        for e in LIST:
            txt += f"{n}{SYMBOL}{e}\n"
            n += 1
        return txt
    
    def add_options_text(self, text, 
            LIST):
        list_txt = self.write_as_list(
            LIST
        )
        result = text + "\n\nelige:\n"\
            + list_txt
        return result

    def add_window_listener(self):
        def fn(idx):
            is_end = self.model.request(
                    "get_is_end", {})
            render_dict = self.model.request(
                "get_render", {})
            k = render_dict\
                ["SCENE_KEYS"][idx]
            self.model.request(
                "set_key",
                {"key": k}
            )
            self.update()
        
        self.window.add_key_listener(
            "1", lambda e:fn(0)
        )
        self.window.add_key_listener(
            "2", lambda e:fn(1)
        )
        self.window.add_key_listener(
            "3", lambda e:fn(2)
        )
        self.window.add_key_listener(
            "4", lambda e:fn(3)
        )
        self.window.add_key_listener(
            "5", lambda e:fn(4)
        )
        
    def update(self):
        render_dict = self.model.request(
            "get_render", {})
        title = self.model.request(
            "get_nif_name", {})
        self.text_area.set_title(
            title
        )
        paragraph = Btpy.sort_text(
            render_dict["TEXT"],
            90
        )
        text = self.add_options_text(
            paragraph,
            render_dict["SCENE_KEYS"]
        )
        self.text_area.set_value(
            text
        )

    def start_nif(self):
        self.model.request(
            "start_nif", {}
        )
        self.model.request(
            "set_is_end",
            {"bool":False}
        )
        self.update()
    
    def start(self):
        self.window.start()