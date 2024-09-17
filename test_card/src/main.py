


from Model import Model 
from View import View
from Card import Card

def main():
    model = Model()
    view = View()
    card_list = []
    for i in range(6):
        card_list.append(Card())
    view.draw_card_field(card_list)
    view.start()

main()