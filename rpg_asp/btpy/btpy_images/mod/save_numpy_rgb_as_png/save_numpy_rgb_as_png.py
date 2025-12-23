


from PIL import Image

def save_numpy_rgb_as_PNG(
        numpy_image_RGB, name:str)->None:
    Image.fromarray(numpy_image_RGB)\
        .save(f"{name}.png")