from PIL import Image

img = Image.open(r"demo.jpg")
img.resize((512, 512)).save("1.jpg")
