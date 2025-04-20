

from btpy.Btpy import Btpy
from clarify_image_pil import*

def main():
    window = Btpy.Window("animator")
    btn = Btpy.Button(window, "save")
    btn.pack()
    canvas = Btpy.Canvas(window, "canvas")
    canvas.set_size(500, 500)
    canvas.pack()
    last_point = [0, 0]
    new_point = [0, 0]
    first_click = False
    buffer_image = None
    def fn(e):
        nonlocal last_point, new_point,\
            first_click, buffer_image
        # reacciona al primer click
        if(not first_click):
            first_click = True
            cursor_point = canvas\
                .get_point_cursor()
            canvas.draw_point(cursor_point)
            last_point = cursor_point
            return None
        new_point = canvas\
            .get_point_cursor()
        canvas.draw_line(
            new_point,
            last_point
        )
        last_point = new_point
    canvas.add_right_click_listener(
        fn
    )
    # button listener
    def fn(e):
        nonlocal buffer_image
        image = canvas\
            .get_image_reflection()
        print("save image")
        buffer_image = image.copy()
        buffer_image = clarify_image_pil(
            buffer_image, 5.0)
        image.save("image_test.png", 
            "PNG")
        canvas.repaint()
        canvas.image_reflection = Image.new(
            'RGBA', 
            (500, 500), 
            (0, 0, 0, 0)
        )
        canvas.set_size(500, 500)
        canvas.draw_image([0, 0],
                buffer_image)
    btn.add_listener(fn)
    window.start()

main()