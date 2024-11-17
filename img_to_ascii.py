# -*- coding: utf-8 -*-
"""IMG_TO_ASCII.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TfdFEzD70hqPLDiSumWUTvkzTQ7B3lCp
"""

from PIL import Image
from google.colab import files

# List of ASCII characters
ASCII_CHARS = [".", ",", ":", ";", "+", "*", "?", "%", "$", "#", "@"]

# Resize the images
def resize(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

# Turn image into grayscale
def gray(image):
    grayscale_image = image.convert("L")
    return grayscale_image

# Convert each pixel into an ASCII character
def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = ""
    shade_f = 255 // (len(ASCII_CHARS) - 1 ) # Calculates the color shade factor
    for pixel in pixels:
        characters += ASCII_CHARS[min(pixel // shade_f, len(ASCII_CHARS) - 1)]
    return characters   # Divides each pixel by the factor and assigns a char.

# Create the ASCII image
def create_ascii_image(new_image_data, new_image_width):
    ascii_image = ""
    for i in range(0, len(new_image_data), new_image_width):
        line = new_image_data[i:i + new_image_width]
        doubled_line = "".join([char * 2 for char in line])
        ascii_image += doubled_line + "\n"
    return ascii_image

if __name__ == "__main__":
    uploaded = files.upload()                                      # Load image

    inv = "No"
    if inv == ("Yes" or "Y"):                         # Controls color inversion
      ASCII_CHARS = ASCII_CHARS[::-1]

    if uploaded:                        # Check if any files have been uploaded
        filename = list(uploaded.keys())[0]                     # Get file name
        try:
            image = Image.open(filename)

            # Convert image into ASCII
            new_image_width = 100
            resized_gray_image = gray(resize(image, new_image_width))
            new_image_data = pixels_to_ascii(resized_gray_image)

            # Format the ASCII image
            ascii_image = create_ascii_image(new_image_data, new_image_width)
            print(ascii_image)

        except:
            print(f"Error opening the image: {e}")
