from PIL import Image, ImageColor
from BackgroundColours import backgroundcolours
import os


def colour_shift(path, bg_replacement, fg_replacement, m_colour, bt, wt, precision):
    """
    Function processes an image spceified in path parameter,
    finds it's background colours and replaces them with the one specified in bg_replacement.

    If, the colour is not on the list, it checks if the colour
    is dark enough to be black in bt variable and if light enough
    to be white.
    """
    img = Image.open(path)
    img = img.convert("RGB")

    # compiling a list of potential background colours
    background = backgroundcolours(img, precision)
    pixels = img.load()

    print("bg " + bg_replacement)
    print("fg " + fg_replacement)
    print("mk " + m_colour)

    background_colour = ImageColor.getrgb(bg_replacement)
    foreground_colour = ImageColor.getrgb(fg_replacement)
    mark_colour       = ImageColor.getrgb(m_colour)
    # colour substitution
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            for colour in background:

                # replacing background colours
                if pixels[x, y] == colour:
                    pixels[x, y] = background_colour
                    continue

                # replacing dark pixels to true black colour
                elif black_supposedly(pixels[x, y], bt):
                    pixels[x, y] = foreground_colour
                    continue

                # replacing light pixels to true white colour
                elif white_supposedly(pixels[x, y], wt):
                    pixels[x, y] = background_colour
                    continue

                # if some colours do not qualify either as a background or foreground
                else:
                    pixels[x, y] = mark_colour

    pure_path = os.path.dirname(path)  # extracts only the directory
    split_path = os.path.splitext(path)[0]  # breaks apart the root and extension
    extension = os.path.splitext(path)[1]  # saving the extension of the file
    filename = split_path.split('/')[-1]  # extract the file name
    processed_file = filename + '_post' + extension  # name of the new file

    final_path = pure_path + '/' + processed_file  # directory + file + extension

    img.save(final_path)
    print("Completed. File saved as " + processed_file)


def black_supposedly(colour, bt):
    """
    Simple verification how close a colour really is to true RGB black
    """
    if colour[0] < int(bt):
        if colour[1] < int(bt):
            if colour[2] < int(bt):
                return True
    else:
        return False


def white_supposedly(colour, wt):
    """
    Simple verification how close a colour really is to true RGB white
    """
    if colour[0] > int(wt):
        if colour[1] > int(wt):
            if colour[2] > int(wt):
                return True
    else:
        return False


