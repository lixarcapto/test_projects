


from model.mod.market.Market import Market
from model.mod.territory.Territory import Territory

def main(): 
    market = Market()
    territory = Territory()
    market = territory.produce_resources(
        market)
    print(territory.write())
    print(market.write())

main()