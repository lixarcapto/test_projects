

from btpy.Btpy import Btpy



def main():
    r = "None"
    #--------------------------------
        

    window = Btpy.Window()
    window.set_full_screen()
    panel_button = Btpy.PanelButton(
        window.widget,
        5, 3)
    panel_button.set_image(
        "../res/image/cell.png"
    )
    panel_button.pack_in_axe()
    window.start()

   
    #------------------------------
    print(r)

main()