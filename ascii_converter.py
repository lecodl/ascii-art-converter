from PIL import Image

ASCII_CHARS = "@%#*+=-:. "

def resize_image(image, new_width=100):
    original_width, original_height=image.size
    aspect_ratio = original_height/original_width
    new_height = int(new_width*aspect_ratio*0.5)
    return image.resize((new_width, new_height))

def convert_to_ascii(image):
    image = image.convert("L")
    pixels = image.getdata()
    ascii_str = ''.join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return ascii_str

def save_art(ascii_str, width, file="output.txt"):
    with open(file, "w") as f:
        for i in range(0, len(ascii_str), width):
            line = ascii_str[i:i+width]
            f.write(line + "\n")

def main(image_path):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Error opening image: {e}")
        return
    new_width = 100
    image = resize_image(image, new_width)
    ascii_str = convert_to_ascii(image)
    save_art(ascii_str, new_width)

if __name__ == "__main__":
    main("input_image.png")