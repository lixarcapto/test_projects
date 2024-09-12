

from btpy.Btpy import Btpy
from btpy.btpy_gui.mod.painter_rmk.Painter import Painter
import datetime



def main():
    r = None
    #--------------------------------
        

    d = Btpy.Duplicate("texto")
    d.set("b")
    def dothis(v):
        d.set("c")
        return v
    r = dothis(d).get()

    """
    date = Btpy.DateEspecial()
    date.hemisphere = date.HEMISPHERE.SOUTH
    date.set_english_date("2024/09/08")
    #for i in range(260):
    #    date.advance_one_day()
    #    print(date.write_narrative())
    r = date.write_narrative()
    """

    #------------------------------
    print(r)

main()