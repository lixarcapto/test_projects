


from btpy.src.btpy.Btpy import Btpy
from Model import Model

class View:

    def __init__(self) -> None:
        self.model = None 
        self.window = Btpy.Window()
        self.window.set_size([700, 500])
        self.button = Btpy.Button(
            self.window)
        self.button.pack_without_expansion(
            self.button.SIDE.TOP
        )
        self.button.set_title(
            "to Phonetic Alphabet")
        self.area = Btpy.Input(self.window)
        self.area.pack_without_expansion(
            self.area.SIDE.TOP
        )
        self.area.set_size(100, 10)
        self.area.set_font("Arial", 12)
        self.area2 = Btpy.Input(self.window)
        self.area2.pack_without_expansion(
            self.area2.SIDE.TOP
        )
        self.area2.set_size(100, 10)
        self.area2.set_font("Arial", 12)
        self.command = ""
        self.add_listener()
        
    def set_model(self, model):
        self.model = model

    def request(self):
        return {
            "command":self.command,
            "text":self.area.get_text()
        }
    
    def receive(self, message):
        self.area2.set_text(message["text"])

    def add_listener(self):
        self.add_listener_afi()

    def add_listener_afi(self):
        def action(e):
            self.command = "to_afi"
            message = self.request()
            self.model.receive(message)
            message = self.model.request()
            self.receive(message)
        self.button.add_click_listener(
            action)

    def start(self):
        self.window.start()