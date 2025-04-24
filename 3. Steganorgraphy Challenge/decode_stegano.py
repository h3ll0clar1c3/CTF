from PIL import Image

def decode_image(encoded_image_path):
    encoded = Image.open(encoded_image_path)
    width, height = encoded.size
    hidden_message = ""

    for row in range(height):
        for col in range(width):
            r, g, b = encoded.getpixel((col, row))
            if b != 0:  # Non-zero blue values indicate hidden data
                hidden_message += chr(b)
            if hidden_message.endswith("}"):  # End of flag
                break
        if hidden_message.endswith("}"):
            break

    print("Hidden message:", hidden_message)

# Usage
decode_image("encoded.png")