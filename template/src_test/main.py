

from app.controller.Controller \
    import Controller
from app.model.Model import Model
from app.view.View import View
from app.persistence.Persistence \
    import Persistence

def main():
    controller = Controller(
        Model(Persistence()), 
        View()
    )

main()