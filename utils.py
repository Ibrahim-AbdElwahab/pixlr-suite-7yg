import os
from PIL import Image

def load_image(image_path):
    """
    Load an image from the specified path.
    
    :param image_path: Path to the image file.
    :return: Loaded PIL Image object or None if there's an error.
    """
    try:
        img = Image.open(image_path)
        return img
    except Exception as e:
        print(f"Error loading image {image_path}: {e}")
        return None

def save_image(image, save_path):
    """
    Save the PIL Image object to the specified path.
    
    :param image: The PIL Image object to save.
    :param save_path: Path where the image will be saved.
    """
    try:
        image.save(save_path)
        print(f"Image saved to {save_path}")
    except Exception as e:
        print(f"Error saving image to {save_path}: {e}")

def get_image_files(directory):
    """
    Get a list of image files in a specified directory.
    
    :param directory: Directory to search for images.
    :return: List of image file paths.
    """
    image_files = []
    valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')

    # Check if directory exists
    if not os.path.isdir(directory):
        print(f"Directory {directory} does not exist.")
        return image_files

    for filename in os.listdir(directory):
        if filename.lower().endswith(valid_extensions):
            image_files.append(os.path.join(directory, filename))

    return image_files

def resize_image(image, new_width, new_height):
    """
    Resize the given PIL Image to the new dimensions.
    
    :param image: The PIL Image object to resize.
    :param new_width: Desired width.
    :param new_height: Desired height.
    :return: Resized PIL Image object.
    """
    try:
        resized_image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
        return resized_image
    except Exception as e:
        print(f"Error resizing image: {e}")
        return None

# TODO: Add functionality for maintaining aspect ratio
# TODO: Implement a logging system instead of print statements
# TODO: Add support for more image formats and error handling for unsupported formats

# If you're feeling adventurous, you can also add a feature to
# create a thumbnail or apply filters to the images!
