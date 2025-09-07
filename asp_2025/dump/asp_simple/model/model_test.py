

from .market.Market import Market

def model_test():
    print("--> model_test")
    market = Market()
    market.sum_value("gasoline", 2)
    market.sum_value("gasoline", -6)
    print(market.write())