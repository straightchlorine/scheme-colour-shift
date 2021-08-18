from PIL import Image, ImageEnhance, ImageColor
import numpy as np
from MainColours import *
import sys

#img = Image.open(sys.argv[1])
img = Image.open("/home/goldberg/current_project/colour-change/images/page.jpg")
img = img.convert("RGB")

# compiling a list of potential background colours
background = background(img)

# creating an array of pixels
pixels = img.load()

white = ImageColor.getrgb("white")
black = ImageColor.getrgb("black")

# substituting the background colours to white
for x in range(img.size[0]):
    for y in range(img.size[1]):
        for colour in background:
            if pixels[x, y] == colour:
                pixels[x, y] = white
img.save("/home/goldberg/current_project/colour-change/images/page_redone.jpg")
print("Process finished, and image is saved")
