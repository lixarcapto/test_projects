


from app.model.Model import Model
from app.view.View import View
from app.controller.Controller import Controller
from app.persistence.Persistence import Persistence

def main():
    controller = Controller(
        View(), 
        Model(Persistence()))
    

main()