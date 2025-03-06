


import pyautogui
import time
import mouse #pip install mouse

def create_path_bot():
    point_list:list[int] = []
    is_active = False
    was_unactive = False
    while True:
        if mouse.is_pressed(button='left'):
            if(is_active):
                x, y = pyautogui.position()
                print([x, y])
                point_list.append([x, y])
                time.sleep(0.1) # Debounce, to prevent multiple readings of the same click.
        if mouse.is_pressed(button='right'): #or 'right' or 'middle'
            if(is_active):
                print("is_not_active")
                is_active = False
                was_unactive = True
            if(not is_active):
                print("is_active")
                is_active = True
        time.sleep(0.01) # Check mouse state every 10 milliseconds.
        if(was_unactive): break
    print(point_list)