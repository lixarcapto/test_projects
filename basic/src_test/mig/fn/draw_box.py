


import numpy as np

def draw_box(image, point, size, color):
    """
    Draws a box around a point in an RGB image.

    Args:
        image (numpy.ndarray): The input RGB image.
        point (tuple): The (x, y) coordinates of the point.
        size (int): The size of the box in pixels.
        color (tuple): The RGB color of the box.

    Returns:
        numpy.ndarray: The modified RGB image with the box drawn.
    """

    x, y = point
    half_size = size // 2

    # Check for valid point and box size
    if x < 0 or x >= image.shape[1] or y < 0 or y >= image.shape[0]:
        raise ValueError("Invalid point or box size")

    if size <= 0:
        raise ValueError("Box size must be greater than 0")

    # Draw the top and bottom lines of the box
    image[y - half_size:y + half_size + 1, x, :] = color
    image[y, x - half_size:x + half_size + 1, :] = color

    # Fill the inside of the box
    image[y - half_size:y + half_size + 1, x - half_size:x + half_size + 1, :] = color

    return image