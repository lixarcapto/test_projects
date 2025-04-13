

from btpy.Btpy import Btpy
import webbrowser

"""
def main():
    print("init...")
    window = Btpy.Window("ventana")
    label_pet = Btpy.LabelImage(window)
    label_pet.grid(0, 0)
    button = Btpy.ButtonIcon(
        window, "feed", 
        "./res/image/pet/rat_100x100.png")
    button.grid(1, 0)
    limit_n = Btpy.LimitNumber(
        13, [0, 19]
    )
    range_dict = {
        "pet_ocfat_angry.png":[0, 5],
        "pet_ocfat_sad.png":[6, 10],
        "pet_ocfat_normal.png":[11, 15],
        "pet_ocfat_happy.png":[16, 19]
    }
    def update():
        nonlocal range_dict, limit_n, \
            label_pet
        image_name = Btpy.whats_range(
            range_dict,
            limit_n.get()
        )
        if(image_name[0] == 
                "pet_ocfat_angry.png"):
             webbrowser.open_new_tab(
                 "https://www.youtube.com/watch?v=UWEhMH-LfMI")
        label_pet.set_path_image(
            "./res/image/pet/" 
            + image_name[0])
    def fn_repeat(n):
        limit_n.sum(-1)
        update()
    Btpy.repeat_each_async(5, fn_repeat)
    def fn(e):
        nonlocal range_dict, limit_n, \
            label_pet
        limit_n.sum(1)
        update()
    button.add_listener(fn)
    window.start()
"""

from View import View

def main():
    view = View()
    view.start()

main()