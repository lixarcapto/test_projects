

from btpy.Btpy import Btpy




def main():
    r = None
    #--------------------------------
        


    window = Btpy.Window()
    window.set_size(1200, 700)
    painter = Btpy.Painter(window)
    painter.pack_in_axe()
    painter.draw_text("hola mundo", [100, 100])
    painter.draw_circle([0,0], [500, 300])
    window.start()

    #------------------------------
    print(r)

main()