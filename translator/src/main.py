

from btpy.src.btpy.Btpy import Btpy
from Model import Model
from View import View

def main():
    view = View()
    view.set_model(Model())
    view.start()

main()