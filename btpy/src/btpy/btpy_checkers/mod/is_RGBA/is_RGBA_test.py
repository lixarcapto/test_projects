


from is_RGBA import*

def main():
    #
    r = is_RGBA([255, 255, 255, 0.4])
    print(r == True)
    #
    r = is_RGBA([255, 255, 255, 255])
    print(r == False)
    #
    r = is_RGBA([255, 255, 255, 0])
    print(r == True)
    #
    r = is_RGBA([255, 255, 255, 0.999])
    print(r == True)
    #
    r = is_RGBA([255, 255, 255, 1])
    print(r == True)
    #
    r = is_RGBA([256, 255, 255, 0.4])
    print(r == False)
    #
    r = is_RGBA([255, 255, 255, -1])
    print(r == False)
    #
    r = is_RGBA([255, 255, -255, 0])
    print(r == False)
    #

main()