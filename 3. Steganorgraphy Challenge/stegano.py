# File: stegano.py
from PIL import Image

def encode_image(input_image_path, output_image_path, secret_message):
    image = Image.open(input_image_path)
    encoded = image.copy()
    width, height = image.size
    index = 0

    for row in range(height):
        for col in range(width):
            if index < len(secret_message):
                r, g, b = image.getpixel((col, row))
                encoded.putpixel((col, row), (r, g, ord(secret_message[index])))
                index += 1

    encoded.save(output_image_path)

# Usage
encode_image("input.jpg", "encoded.png", "CTF{hidden_flag}")