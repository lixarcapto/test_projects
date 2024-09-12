

from btpy.Btpy import Btpy


def main():
    r = None
    #--------------------------------
        
   

    window = Btpy.Window()
    window.set_size([400, 700])
    label = Btpy.Label(window)
    label.set_text("a")
    label.pack_without_expansion()
    label2 = Btpy.Label(window)
    label2.set_text("b")
    label2.pack_without_expansion()
    window.start()

    #------------------------------
    print(r)

main()