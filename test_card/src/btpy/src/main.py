

from btpy.Btpy import Btpy

def main():
    r = "None"
    #--------------------------------

    scenario = Btpy.Scenario()
    scenario.set_size(1300, 700)
    go1 = scenario.GObject()
    window = Btpy.Window()
    window.set_full_screen()
    window.add_close_action(
        lambda :print("funciona"))
    window.start()

   
    #------------------------------
    print(r)

main()