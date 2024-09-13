

from btpy.Btpy import Btpy



def main():
    r = "None"
    #--------------------------------
        
    
    scenario = Btpy.Scenario()
    scenario.set_size(1200, 1200)
    g1 = scenario.GObject()
    g1.set_route_image(
        "../res/image/cell.png")
    g1.move_arrow = [40, 0]
    scenario.add(g1)
    window = Btpy.Window()
    window.set_full_screen()
    painter = Btpy.Painter(window)
    painter.pack_in_axe()
    def action(i):
        painter.repaint()
        scenario.update()
        painter.draw_image_dict(
            g1.get_image_paint_dict()
        )
        print("repeat"+ str(i))
    Btpy.repeat_each_async(2, action)
    window.start()

    #------------------------------
    print(r)

main()