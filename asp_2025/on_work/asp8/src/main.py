


from app.model.Model import Model
from app.view.View import View
from app.controller.Controller import Controller
from btpy.src.btpy.Btpy import Btpy
from app.persistence.Persistence import Persistence

def main():
    print("init...")

    controller = Controller(View(), Model())
    controller.start()

main()