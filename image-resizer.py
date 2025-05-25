from PIL import Image
import os

def resize(im, new_width):
    width, height = im.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = im.resize((new_width, new_height))
    return resized_image

files = os.listdir("Photo")
extensions = ["jpg", "jpeg", "png", "ico", "gif"]

for file in files:
    extension = file.split(".")[-1].lower()
    if extension in extensions:
        im = Image.open(os.path.join("Photo", file))
        resized_image = resize(im, 400)
        filepath = os.path.join("Photo", f"{file}(resized).jpg")
        resized_image.save(filepath)


