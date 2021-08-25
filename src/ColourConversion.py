from PIL import Image, ImageColor
from BackgroundColours import BackgroundData
import os


class Conversion:
    """
    Class receives an array of parameters, based on those parameters it
    accordingly modifies given image.
    """
    param_data = None

    def __init__(self, params):
        self.param_data = params

    def colour_shift(self):
        """
        returns void

        Processes the image, and changes the colour of each pixel accordingly.
        """
        # opening the image
        img = Image.open(self.param_data.path_param)
        img = img.convert("RGB")

        # compiling a list of potential background colours
        bg = BackgroundData(self.param_data)
        background = bg.background_colours(img)
        pixels = img.load()

        print("Process started...")

        # colour substitution
        for x in range(img.size[0]):
            for y in range(img.size[1]):
                for colour in background:

                    # replacing background colours
                    if pixels[x, y] == colour:
                        pixels[x, y] = ImageColor.getrgb(self.param_data.bg_c_param)
                        break

                    # replacing dark pixels to true black colour
                    elif self.black_supposedly(pixels[x, y]):
                        pixels[x, y] = ImageColor.getrgb(self.param_data.fg_c_param)
                        break

                    # replacing light pixels to true white colour
                    elif self.white_supposedly(pixels[x, y]):
                        pixels[x, y] = ImageColor.getrgb(self.param_data.bg_c_param)
                        break

                    # if some pixels did not meet any requirement
                    else:
                        pixels[x, y] = ImageColor.getrgb(self.param_data.mk_c_param)
                        break

        p_dir = os.path.dirname(self.param_data.path_param)     # directory
        raw = os.path.splitext(self.param_data.path_param)[0]   # only dir + filename
        ext = os.path.splitext(self.param_data.path_param)[1]   # extension
        f_name = raw.split('/')[-1]                             # file name

        p_name = f_name + '_processed' + ext  # processed name
        f_path = p_dir + '/' + p_name         # final path

        img.save(f_path)
        img.close()
        print("Completed. File saved as " + p_name + " in " + p_dir)

    def black_supposedly(self, colour):
        """
        returns True, if the colour is dark enough.

        If every parameter(R, G and B) is less than or equal to the black threshold
        """
        if colour[0] <= self.param_data.bt_param:
            if colour[1] <= self.param_data.bt_param:
                if colour[2] <= self.param_data.bt_param:
                    return True
        else:
            return False

    def white_supposedly(self, colour):
        """
        returns True, if the colour is light enough.

        If every parameter(R, G and B) is more than or equal to the black threshold
        """
        if colour[0] >= self.param_data.wt_param:
            if colour[1] >= self.param_data.wt_param:
                if colour[2] >= self.param_data.wt_param:
                    return True
        else:
            return False
