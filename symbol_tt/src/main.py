

from btpy.src.btpy.Btpy import Btpy
from view.View import View

def main():
    view = View()
    view.draw_symbols(["flower", "flower"])
    view.start()

main()