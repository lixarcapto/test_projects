

from model.Model import Model
from btpy.Btpy import Btpy

class View:

    def __init__(self):
        self.model = Model()
        self.window = Btpy.Window(
            "NIF reader")
        self.window.set_size(1000, 700)
        self.frame_head = None
        self.title_nif = None
        self.input_file = None
        self.button_read = None
        self.button_reset = None
        self.text_area = None
        self.radio_box = None
        # ------------------------------
        self.init_frame_head()
        self.init_text_area()
        
    def init_text_area(self):
        self.text_area = Btpy.TextArea(
            self.window, "Nif actual"
        )
        self.text_area.pack(False, "left")
        self.radio_box = Btpy.RadioBox(
            self.window, 
            "Elige una opcion:"
        )
        self.radio_box.pack(False, "left")

    def init_frame_head(self):
        self.frame_head = Btpy.Frame(
            self.window)
        self.frame_head.pack(False, "top")
        self.frame_head.set_background_color(
            "yellow")
        self.title_nif = Btpy.LabelImage(
            self.frame_head
        )
        self.title_nif.set_path_image(
            "./res/image/nif_icon.png")
        self.title_nif.pack(False, 
            "left")
        self.input_file = Btpy.InputFile(
            self.frame_head, "text", 
            "NIF path"
        )
        self.input_file.pack(False, 
            "left")
        self.button_read = Btpy.Button(
            self.frame_head)
        self.button_read.set_title("Read")
        self.button_read.pack(False, 
            "left")
        self.button_reset = Btpy.Button(
            self.frame_head)
        self.button_reset.set_title("Reset")
        self.button_reset.pack(False, 
            "left")
        def fn(e):
            self.load_and_start()
        self.button_read.add_listener(fn)
        def fn(e):
            self.start_nif()
        self.button_reset.add_listener(fn)

    def load_and_start(self):
        v = self.input_file.get_value()
        self.model.request(
            "load_nif_file",
            {"path": v}
        )
        self.start_nif()
        self.update()
        
    def update(self):
        render_dict = self.model.request(
            "get_render", {})
        title = self.model.request(
            "get_nif_name", {})
        self.text_area.set_title(
            title
        )
        self.text_area.set_value(
            render_dict["TEXT"]
        )
        if(self.model.request(
                    "get_is_end", {})): 
            self.hidde_radio_box()
            return None
        self.radio_box.set_content(
            render_dict["SCENE_KEYS"]
        )
        value = self.radio_box\
                .get_value()
        def fn():
            value = self.radio_box\
                .get_value()
            self.model.request(
                "set_key",
                {"key": value}
            )
            self.update()
        self.radio_box\
            .add_on_change_listener(fn)

    def start_nif(self):
        self.model.request(
            "start_nif", {}
        )
        if(self.model.request(
                    "get_is_end", {})):
            self.show_radio_box()
        self.model.request(
            "set_is_end",
            {"bool":False}
        )
        self.update()

    def hidde_radio_box(self):
        self.radio_box.pack_forget()

    def show_radio_box(self):
        self.radio_box.pack()
    
    def start(self):
        self.window.start()