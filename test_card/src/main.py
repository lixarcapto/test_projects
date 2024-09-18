


from Model import Model 
from View import View
from Card import Card
from btpy.src.btpy.Btpy import Btpy

def main():
    model = Model()
    view = View()
    message = model.render()
    view.receibe(message)
    view.start()

main()