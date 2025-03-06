

from is_RGB import*

def main():
    print("--> is_rgb_test")
    #
    r = is_RGB([255, 255, 255])
    print(r == True)
    #
    r = is_RGB([255, 255, 256])
    print(r == False)
    #
    r = is_RGB([255, 255, 255, 255])
    print(r == False)
    #
    r = is_RGB([0, 0, 0])
    print(r == True)
    #
    r = is_RGB([-1, 255, 255])
    print(r == False)
    #
    r = is_RGB(["255", 255, 255])
    print(r == False)
    #
    r = is_RGB([255, 255, 255])
    print(r == True)
    #
    r = is_RGB([255.0, 255, 255])
    print(r == False)
    #
    r = is_RGB([255, 255])
    print(r == False)
    #

main()
    