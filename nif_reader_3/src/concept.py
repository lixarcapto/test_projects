

from btpy.src.btpy.Btpy import Btpy

def main():
    window = Btpy.Window()
    window.set_full_screen()
    label = Btpy.Label(window)
    label.pack_in_axe(label.AXE_EXPANSION.X)
    label.set_image("./chica_en_restaurante.png")
    window.start()

main()