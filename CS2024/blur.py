from PIL import Image, ImageFilter

before = Image.open("udon.bmp")
after = before.filter(ImageFilter.BoxBlur(10))
after.save("out.bmp")