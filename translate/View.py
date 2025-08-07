

from btpy.Btpy import Btpy

class View:

    DICT = {
        "á":"ɑ:",
        "a'":"ʌ",
        "ó":"ɒ",
        "dd":"ð",
        "é":"æ",
        "ä":"ə",
        "ä:":"ɜ",
        "í":"ɪ",
        "l'":"ɫ",
        "n'":"ŋ",
        "o":"ɔ",
        "r":"ɹ",
        "r'":"ʳ",
        "sh":"ʃ",
        "ch":"tʃ",
        "t'":"t̮",
        "ú":"ʊ",
        "dj":"dʒ",
        "j":"ʒ"
    }

    def __init__(self):
        self.window = Btpy.Window(
            "titulo"
        )
        self.button_translate = Btpy\
            .Button(
            self.window, "translate"
        )
        self.button_translate.pack()
        self.input_raw = Btpy.TextArea(
            self.window, "ingresa"
        )
        self.input_raw.set_size(
            30, 10
        )
        self.input_raw.pack()
        self.input_process = Btpy.TextArea(
            self.window, "ingresa"
        )
        self.input_process.pack()
        self.input_process.set_size(
            30, 10
        )
        def fn(e):
            text = self.input_raw.get_value()
            text = self.translate_text(
                text)
            self.input_process.set_value(
                text)
        self.button_translate.add_listener(
            fn
        )
        self.window.start()

    def translate_text(self, text):
        for k in View.DICT:
            text = text.replace(
                k, View.DICT[k])
        return text