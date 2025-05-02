

from basic.Basic import Basic

def main():
    r = ""

    crono = Basic.crono()
    Basic.pause(10)
    r = crono.stop()

    print(r)

main()