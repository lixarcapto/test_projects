

from btpy.Btpy import Btpy

def main():
    r = ""

    crono = Btpy.crono()
    Btpy.pause(10)
    r = crono.stop()

    print(r)

main()