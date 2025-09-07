

from data_access.DataAccess import DataAccess
from data_model.firm.product.market_product.EconomicProduct import EconomicProduct
from data_model.app.person_list_lib.core.body.app.task.metabolism_task.DoesntHaveToiletPaperTk import DoesntHaveToiletPaperTk

class ConsumeProductTk: #comprar productos en el mercado

    def inner(self, personProduct, marketGlobalProduct):
        goodsKeysData = DataAccess().getGoodsKeysData()
        economicProduct = EconomicProduct()
        doesnHaveToiletPaper = DoesntHaveToiletPaperTk()
        goods = None
        if(not personProduct.needs.hasToiletPaper):
            if(marketGlobalProduct.hasGoods(goodsKeysData.TOILET_PAPER)):
                goods = marketGlobalProduct.getGoods(goodsKeysData.TOILET_PAPER)
                personProduct.needs.hasToiletPaper = True
        #PROTEIN
        if(not personProduct.needs.hasProtein):
            if(marketGlobalProduct.hasGoods(goodsKeysData.COW_MEAT)):
                goods = marketGlobalProduct.getGoods(goodsKeysData.COW_MEAT)
                personProduct.needs.hasProtein = True
            elif(marketGlobalProduct.hasGoods(goodsKeysData.PIG_MEAT)):
                goods = marketGlobalProduct.getGoods(goodsKeysData.PIG_MEAT)
                personProduct.needs.hasProtein = True
            elif(marketGlobalProduct.hasGoods(goodsKeysData.TURKEY_MEAT)):
                goods = marketGlobalProduct.getGoods(goodsKeysData.TURKEY_MEAT)
                personProduct.needs.hasProtein = True
            elif(marketGlobalProduct.hasGoods(goodsKeysData.WILD_MEAT)):
                goods = marketGlobalProduct.getGoods(goodsKeysData.WILD_MEAT)
                personProduct.needs.hasProtein = True
        #
        if(not personProduct.needs.hasToiletPaper):
            if(marketGlobalProduct.hasGoods(goodsKeysData.TOILET_PAPER)):
                goods = marketGlobalProduct.getGoods(goodsKeysData.TOILET_PAPER)
                personProduct.needs.hasToiletPaper = True
        economicProduct.marketGlobalProduct = marketGlobalProduct
        economicProduct.personProduct = personProduct
        return economicProduct
