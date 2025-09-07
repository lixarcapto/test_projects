

from model.mod.citizen.Citizen import Citizen
from model.mod.citizen.citizen_constants import*
from btpy.Btpy import Btpy
from model.mod.market.Market import Market

def main():
    citizen1:Citizen = Citizen()
    citizen1.randomize_legendary(
        "north_sailors", "female")
    citizen1.advance_one_month(None, False)
    print(citizen1.write())

main()