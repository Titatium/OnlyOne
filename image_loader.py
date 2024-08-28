from PIL import Image, ImageTk

def load_image(filename):
    """
    Loads an image file using PIL (Pillow).

    Args:
        filename (str): The path to the image file.

    Returns:
        Image: The loaded PIL Image object.
    """
    try:
        image = Image.open(filename)
        return image
    except FileNotFoundError:
        print(f"Error: Image file not found: {filename}")
        return None
    except IOError:
        print(f"Error: Unable to open image file: {filename}")
        return None

def resize_image(image, width, height):
    """
    Resizes a PIL Image object to the specified dimensions.

    Args:
        image (Image): The PIL Image object to resize.
        width (int): The desired width.
        height (int): The desired height.

    Returns:
        Image: The resized PIL Image object.
    """
    resized_image = image.resize((width, height), Image.ANTIALIAS)
    return resized_image

def convert_to_tk_image(image):
    """
    Converts a PIL Image object to a Tkinter-compatible PhotoImage.

    Args:
        image (Image): The PIL Image object to convert.

    Returns:
        PhotoImage: The Tkinter PhotoImage object.
    """
    photo = ImageTk.PhotoImage(image)
    return photo