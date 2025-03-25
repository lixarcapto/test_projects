



from btpy.src.btpy.Btpy import Btpy
import os

class View:

    def __init__(self) -> None:
        self.size_x = 100
        self.size_y = 100
        self.limit_x = 1100
        self.limit_y = 500
        self.back_route = "../res/"
        self.extension = ".png"
        self.symbol_arr = ""
        self.window = Btpy.Window()
        self.window.set_size([700, 500])
        self.painter = Btpy.Painter(
            self.window)
        self.painter.pack_in_axe(
        self.painter.AXE_EXPANSION.BOTH)
        self.painter.set_background("white")
        self.painter.data.background_color = "white"
        self.button = Btpy.Button(
            self.window)
        self.button.pack_without_expansion(
            self.button.SIDE.BOTTOM
        )
        self.button.set_title("translate")
        self.area = Btpy.Input(self.window)
        self.area.pack_without_expansion(
            self.button.SIDE.BOTTOM
        )
        self.area.set_font("Arial", 12)
        self.second_init()

    def second_init(self):
        def action(e):
            text = self.area.extract_text()
            text = text.replace("\n", "")
            self.translate_to_symbols(
                text)
        self.button\
            .add_click_listener(action)

    def translate_to_symbols(self, TEXT):
        words_arr = Btpy.get_words(TEXT)
        self.draw_symbols(words_arr)

    def draw_symbols(self, SYMBOL_ARR):
        self.painter.repaint()
        x = 0
        y = 0
        route = ""
        for symbol in SYMBOL_ARR:
            route = self.back_route \
                + symbol + ".png"
            if(not os.path.exists(route)):
                continue
            self.painter.draw_image(
                route,
                x, y
            )
            x += self.size_x
            if(self.size_x >= self.limit_x):
                x = 0
                y += self.size_y

    def start(self):
        self.window.start()