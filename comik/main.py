
from btpy.Btpy import Btpy
from Model import Model

class View:

    IMAGE_FORMAT = ".png"

    def create_new_vignette(self)->dict:
        list_ = []
        for i in range(self.model.layouts_text):
            list_.append("")
        self.buffer_text = list_
        self.model.create_new_vignette()
        max_idx = self.model\
            .get_vignette_list_size() -1
        self.swiper.set_content(
            [0, max_idx]
        )
        self.swiper.set_value(max_idx)
        self.vignette_index = max_idx

    def create_buffer_text(self):
        list_ = []
        for i in range(self.model.layouts_text):
            list_.append("")
        self.buffer_text = list_

    def __init__(self):
        self.model = Model()
        self.vignette_list = []
        self.buffer_text = []
        self.comik_name = "new"
        self.vignette_index:list = 0
        self.window = Btpy.Window("titulo")
        self.canvas = Btpy.Canvas(
            self.window,
            "canvas"
        )
        self.canvas.pack()
        self.canvas.set_size(650, 650)
        self.window.set_size(1200, 650)
        # ----------------------------
        self.frame = Btpy.Frame(
            self.window)
        self.frame.pack()
        self.swiper = Btpy.SwiperRange(
            self.frame,
            "vignette",
            [0, 1]
        )
        self.swiper.grid(0, 0)
        self.swiper_txt_layout = Btpy.SwiperRange(
            self.frame,
            "text layout",
            [0, self.model.layouts_text]
        )
        self.swiper_txt_layout.grid(0, 1)
        def fn(e):
            self.update()
        self.swiper.add_listener(fn)
        self.input_name_img = Btpy\
            .InputFile(
                self.frame, 
                "image",
                "image"
            )
        self.input_name_img.grid(0, 2)
        self.input_name = Btpy.TextField(
            self.frame, "name"
        )
        self.input_name.grid(0, 3)
        self.button_new_vignette = Btpy.Button(
            self.frame, "new vignette")
        self.button_new_vignette\
            .grid(0, 4)
        def fn(e):
            self.create_new_vignette()
            self.update()
        self.button_new_vignette\
            .add_listener(fn)
        self.button_save_image = Btpy.Button(
            self.frame, "save image")
        self.button_save_image.grid(0, 5)
        def fn(e):
            self.save_image_vignette()
            self.update()
        self.button_save_image\
            .add_listener(fn)
        # ------------------------------
        self.input_text = Btpy.TextArea(
            self.frame, "text"
        )
        self.input_text.set_size(12, 3)
        self.input_text.grid(0, 6)
        # ------------------------------
        self.btn_reset = Btpy.Button(
            self.frame, "reset"
        )
        self.btn_reset.grid(0, 7)
        def fn_reset(e):
            self.model.reset()
            self.update()
        self.btn_reset.add_listener(
            fn_reset
        )
        # ---------------------------
        self.button_save = Btpy.Button(
            self.frame, "save"
        )
        self.button_save.grid(0, 8)
        def fn_save(e):
            self.save_comik_folder()
            print("save")
        self.button_save.add_listener(
            fn_save)
        # ----------------------------
        def click_save(e):
            pt = self.canvas\
                .get_point_cursor()
            self.save_buble_text()
            print(pt)
            self.update()
        self.canvas.add_right_click_listener(
            click_save
        )
        self.canvas.set_fill_color("white")
        self.canvas.set_brush_color(
                "black")
        self.create_new_vignette()
        def fn(e):
            self.remember_last_text()
            self.model.actual_layout_text\
                = self.swiper_txt_layout\
                    .get_value()
            self.update()
        self.swiper_txt_layout\
            .add_listener(fn)
        
    def remember_last_text(self):
        idx = self.model.actual_layout_text
        text = self.input_text.get_value()
        self.buffer_text[idx] = text
        print(self.buffer_text)
        
    def update_input_text(self):
        idx = self.model\
            .actual_layout_text
        text = self.buffer_text[idx]
        self.input_text.set_value(text)
        self.input_text\
            .set_is_enabled(True)

    def save_buble_text(self):
        self.remember_last_text()
        text = self.input_text.get_value()
        self.input_text.set_value("")
        self.input_text.set_is_enabled(
            True)
        print("buffer_text", self.buffer_text)
        self.add_text_buble(
            self.buffer_text)
        self.create_buffer_text()

    def save_comik_folder(self):
        name = self.input_name.get_value()
        if(name == ""):
            self.comik_name = "new"
        else:
            self.comik_name = name
        Btpy.create_folder(
            "./comik/" + self.comik_name
        )
        path = "./comik/"\
            + self.comik_name + "/"\
            + "json.json"
        Btpy.write_json_object(
            path,
            self.vignette_list
        )

    def add_text_buble(self, TEXT:str):
        self.model.create_buble_text(
            self.canvas.get_point_cursor(),
            TEXT
        )

    def update(self):
        idx = self.swiper.get_value()
        self.model.set_vignette_index(
            idx
        )
        self.update_vignette()
        self.update_input_text()
        
    def draw_buble_text(self):
        buble_text_list = self.model\
            .get_buble_text_list()
        layout = self.model.actual_layout_text
        print("buble_text_list", buble_text_list)
        for dict_ in buble_text_list:
            self.canvas.draw_rectangle(
                dict_["POINT_LIST"],
                20 * len(dict_["TEXT_LAYOUT"][layout]), 
                50
            )
            self.canvas.draw_text(
                dict_["POINT_LIST"],
                dict_["TEXT_LAYOUT"][layout]
            )

    def save_image_vignette(self):
        path = self.input_name_img\
            .get_value()
        name = Btpy.find_file_name(path)
        new_path = self.get_image_folder()\
            + name + View.IMAGE_FORMAT
        self.model.set_image_name(name)
        # copia la imagen en la carpeta
        Btpy.copy_file(
            path,
            new_path
        )
        
    def get_image_folder(self):
        return "./" + "comik" + "/"\
        + self.comik_name + "/"
        
    def update_vignette(self):
        self.canvas.repaint()
        self.draw_image_vignette()
        self.draw_buble_text()

    def draw_image_vignette(self):
        name_img = self.model\
            .get_image_name()
        if(name_img == ""): return None
        init_path = self.get_image_folder()
        self.canvas.draw_path_image(
            [0, 0],
            init_path + name_img 
                + View.IMAGE_FORMAT
        )

    def start(self):
        self.window.start()

def main():
    view = View()
    view.start()

main()