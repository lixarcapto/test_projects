

from PIL import ImageTk, Image
import tkinter

def resize_image(route, range_arr)->str:
    # Create the main window
    # Load the image (original code)
    img_open = Image.open(route)
    # Resize the image (original code)
    img_open = img_open.resize(
        (range_arr[0], range_arr[1])
    )
    new_route = ""
    size = f"{range_arr[0]}x{range_arr[1]}"
    new_route = route.replace(".png", "")
    new_route += f"_resized_{size}.png"
    img_open.save(new_route)
    return new_route