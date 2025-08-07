

from btpy.Btpy import Btpy

class Persistence:

    pass

    def get_price_dict()->dict:
        dict_ =  Btpy\
        .read_xlsx_flat_dict(
            "./res/price.xlsx"
        )
        for k in dict_:
            dict_[k] = float(dict_[k])
        return dict_