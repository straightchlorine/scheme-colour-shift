from PIL import Image, ImageColor
from BackgroundColours import backgroundcolours
import os


def colour_shift(path):
    img = Image.open(path)
    img = img.convert("RGB")

    # compiling a list of potential background colours
    background = backgroundcolours(img)

    # creating an array of pixels
    pixels = img.load()

    white = ImageColor.getrgb("white")
    black = ImageColor.getrgb("black")
    magenta = ImageColor.getrgb("magenta")

    # substituting the background colours to white
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            for colour in background:
                if pixels[x, y] == colour:
                    pixels[x, y] = white
                    continue
                #if black_supposedly(pixels[x, y]):
                #    pixels[x, y] = black
                #    continue
                if white_supposedly(pixels[x, y]):
                    pixels[x, y] = white
                    continue
                else:
                    pixels[x, y] = magenta

    pure_path = os.path.dirname(path)  # extracts only the directory
    split_path = os.path.splitext(path)[0]  # breaks apart the root and extension
    extension = os.path.splitext(path)[1]  # saving the extension of the file
    filename = split_path.split('/')[-1]  # extract the file name
    processed_file = '_' + filename + '_post'  # name of the new file

    final_path = pure_path + '/' + processed_file + extension  # directory + file + extension

    img.save(final_path)
    print("Completed. File saved as " + processed_file)


def black_supposedly(colour):
    if colour[0] < 100:
        if colour[1] < 100:
            if colour[2] < 100:
                return True
    else:
        return False


def white_supposedly(colour):
    if colour[0] > 150:
        if colour[1] > 150:
            if colour[2] > 150:
                return True
    else:
        return False
