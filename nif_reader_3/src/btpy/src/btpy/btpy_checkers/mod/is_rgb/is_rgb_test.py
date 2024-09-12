

from .is_rgb import*

def is_rgb_test():
    print("--> is_rgb_test")
    print(is_rgb([255, 255, 255]) == True)
    print(is_rgb([256, 255, 255]) == False)
    print(is_rgb([255, 255]) == False)
    print(is_rgb([0, 0, 0]) == True)
    print(is_rgb([255, 255, 255, 255]) == False)

def is_rgba_test():
    print("--> is_rgba_test")
    print(is_rgba([255, 255, 255, 255]) == True)
    print(is_rgba([256, 255, 255, 255]) == False)
    print(is_rgba([255, 255, 255]) == False)
    print(is_rgba([0, 0, 0, 0]) == True)