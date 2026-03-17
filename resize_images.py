import os
import sys
from PIL import Image

def resize_image(input_path, output_path, width, height):
    """Resize a single image to the specified width and height."""
    try:
        with Image.open(input_path) as img:
            img = img.resize((width, height), Image.Resampling.LANCZOS)
            img.save(output_path)
            print(f"Resized image saved to: {output_path}")
    except Exception as e:
        print(f"Error resizing image {input_path}: {e}")

def batch_resize_images(input_folder, output_folder, width, height):
    """Resize all images in a folder and save them to an output folder."""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            resize_image(input_path, output_path, width, height)
        else:
            print(f"Skipping non-image file: {filename}")

def main():
    """Main function to parse arguments and initiate batch resizing."""
    if len(sys.argv) != 5:
        print("Usage: python resize_images.py <input_folder> <output_folder> <width> <height>")
        return

    input_folder = sys.argv[1]
    output_folder = sys.argv[2]
    try:
        width = int(sys.argv[3])
        height = int(sys.argv[4])
    except ValueError:
        print("Width and height must be integers.")
        return

    if width <= 0 or height <= 0:
        print("Width and height must be positive integers.")
        return

    batch_resize_images(input_folder, output_folder, width, height)

if __name__ == "__main__":
    main()
