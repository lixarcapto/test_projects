

from btpy.Btpy import Btpy



def main():
    r = "None"
    #--------------------------------
        
    
    scenario = Btpy.Scenario()
    scenario.set_size(1200, 1200)
    g1 = scenario.GObject()
    g1.set_route_image(
        "../res/image/cell.png")
    g1.set_move_arrow([40, 0])
    scenario.add(g1)
    g2 = scenario.GObject()
    g2.set_route_image(
        "../res/image/cell.png")
    g2.set_move_arrow([0, 0])
    g2.set_location(300, 300)
    scenario.add(g2)
    window = Btpy.Window()
    window.set_full_screen()
    painter = Btpy.Painter(window)
    painter.pack_in_axe()
    def action(i):
        painter.repaint()
        painter.draw_image(
            "../res/image/chica_en_la_puerta.png",
            [0, 500])
        scenario.update()
        for go in scenario.gobject_list:
            painter.draw_image_dict(
            go.get_image_paint_dict()
        )
        print(g1.write())
        print("repeat"+ str(i))
    Btpy.repeat_each_async(2, action)
    window.start()

    #------------------------------
    print(r)

main()