

from model.Model import Model
from btpy.Btpy import Btpy

class View:

    def __init__(self):
        self.model = Model()
        self.window = Btpy.Window(
            "NIF reader")
        self.window.set_size(1000, 700)
        self.title_nif = Btpy.LabelImage(
            self.window,
            "./res/image/nif_icon.png"
        )
        self.title_nif.pack()
        self.input_file = Btpy.InputFile(
            self.window, "text", "NIF path"
        )
        self.input_file.pack()
        self.button_read = Btpy.Button(
            self.window)
        self.button_read.set_title("Read")
        self.button_read.pack()
        self.button_reset = Btpy.Button(
            self.window)
        self.button_reset.set_title("Reset")
        self.button_reset.pack()
        self.article = Btpy.Article(
            self.window, "Nif actual"
        )
        self.article.label_title_article\
            .grid_forget()
        self.radio_box = Btpy.RadioBox(
            self.window, "Elige una opcion:"
        )
        self.article.pack()
        self.radio_box.pack()
        def fn(e):
            self.load_and_start()
        self.button_read.add_listener(fn)
        def fn(e):
            self.start_nif()
        self.button_reset.add_listener(fn)

    def load_and_start(self):
        self.model.load_nif_file(
                self.input_file.get_value()
            )
        self.start_nif()
        self.update()
        
    def update(self):
        scene_dict = self.model\
            .get_actual_scene_dict()
        title:str = scene_dict["KEY"]
        title = title.lower()
        title = title.title()
        self.article.set_subtitle(
            title
        )
        self.article.set_content(
            scene_dict["TEXT"]
        )
        if(self.model.is_end): 
            self.hidde_radio_box()
            return None
        self.radio_box.set_content(
            scene_dict["SCENE_KEYS"]
        )
        value = self.radio_box\
                .get_value()
        print("init radio box", value)
        self.radio_box.set_value(
                "INVESTIGAR"
            )
        def fn():
            value = self.radio_box\
                .get_value()
            self.model.set_key(value)
            self.update()
        self.radio_box\
            .add_on_change_listener(fn)

    def start_nif(self):
        self.model.start_nif()
        if(self.model.is_end):
            self.show_radio_box()
        self.model.is_end = False
        self.update()

    def hidde_radio_box(self):
        self.radio_box.pack_forget()

    def show_radio_box(self):
        self.radio_box.pack()
    
    def start(self):
        self.window.start()