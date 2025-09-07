

from model.mod.citizen.Citizen import Citizen
from model.mod.citizen.citizen_constants import*
from btpy.Btpy import Btpy
from model.mod.market.Market import Market

def main():
    citizen1:Citizen = Citizen()
    citizen1.randomize_legendary("north_sailors")
    citizen1.set_gender_key("female")
    citizen2:Citizen = Citizen()
    citizen2.randomize_legendary("north_sailors")
    citizen2.set_gender_key("male")
    market = Market()
    genes = None
    let_go_children = False
    for i in range(140):
        market = citizen1.advance_one_month(
            market)
        market = citizen2.advance_one_month(
            market)
        citizen2 = citizen1.socialize(
            citizen2)
        let_go_children = citizen1\
            .time_to_let_go_children()
        """
        if(citizen1.data.get_is_a_mother()):
            print(citizen1.write())
            break
        """

main()