

from PIL import ImageTk
from PIL import Image
    
def numpy_image_RGB_to_photoimage(
        numpy_image_RGB):
    # Convert the NumPy array to a PIL Image object
    pil_image = Image.fromarray(numpy_image_RGB)
    # Convert the PIL Image to a Tkinter PhotoImage object
    tk_image = ImageTk.PhotoImage(pil_image)
    return tk_image
