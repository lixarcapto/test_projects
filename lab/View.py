

from btpy.src.btpy.Btpy import*

class View:

    def __init__(self) -> None:
        self.window = Btpy.Window()
        self.window.set_size([700, 700])
        self.label = Btpy.Label(self.window)
        self.label.pack_in_axe(
            self.label.AXE_EXPANSION.BOTH)
        self.input = Btpy.Input(self.window)
        self.input.pack_in_axe(
            self.label.AXE_EXPANSION.BOTH)
        
    def receive(self, message):
        self.label.set_image(
            message["image"]
        )

    def get_text(self):
        text = self.input.extract_text()
        return text

    def request(self):
        return {
            "text":self.get_text()
        }

    def start(self):
        self.window.start()