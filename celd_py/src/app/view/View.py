

from btpy.src.btpy.Btpy import Btpy

class View:

    def __init__(self) -> None:
        self.window = Btpy.Window()
        self.window.set_full_screen()
        self.painter = Btpy.Painter(
            self.window)
        self.painter.pack_in_axe(
            self.painter.AXE_EXPANSION.BOTH)
        