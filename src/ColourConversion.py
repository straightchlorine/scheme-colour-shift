from PIL import Image, ImageColor
from BackgroundColours import backgroundcolours
import os


def colour_shift(precision, wt, bt, mark_colour, bg_replacement, fg_replacement, path):
    """
    returns void

    Processes the image, and changes the colour of each pixel accordingly.
    """
    img = Image.open(path)
    img = img.convert("RGB")

    # compiling a list of potential background colours
    background = backgroundcolours(img, precision)
    pixels = img.load()

    print("Process started...")

    # colour substitution
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            for colour in background:

                # replacing background colours
                if pixels[x, y] == colour:
                    pixels[x, y] = ImageColor.getrgb(bg_replacement)
                    break

                # replacing dark pixels to true black colour
                elif black_supposedly(pixels[x, y], bt):
                    pixels[x, y] = ImageColor.getrgb(fg_replacement)
                    break

                # replacing light pixels to true white colour
                elif white_supposedly(pixels[x, y], wt):
                    pixels[x, y] = ImageColor.getrgb(bg_replacement)
                    break

                # if some pixels did not meet any requirement
                else:
                    pixels[x, y] = ImageColor.getrgb(mark_colour)
                    break


    dir   = os.path.dirname(path)       # directory
    raw   = os.path.splitext(path)[0]   # only dir + filename 
    ext   = os.path.splitext(path)[1]   # extension
    fname = raw.split('/')[-1]          # file name

    p_name = fname + '_processed' + ext     # processed name
    f_path = dir + '/' + p_name             # final path

    img.save(f_path)

    print("Completed. File saved as " + p_name + " in " + dir)

    img.close()


def black_supposedly(colour, bt):
    """
    returns True, if the colour is dark enough.

    If every parameter(R, G and B) is less than or equal to the black threshold
    """
    if colour[0] <= int(bt):
        if colour[1] <= int(bt):
            if colour[2] <= int(bt):
                return True
    else:
        return False


def white_supposedly(colour, wt):
    """
    returns True, if the colour is light enough.

    If every parameter(R, G and B) is more than or equal to the black threshold
    """
    if colour[0] >= int(wt):
        if colour[1] >= int(wt):
            if colour[2] >= int(wt):
                return True
    else:
        return False


