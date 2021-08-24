class BackgroundData:
    # attributes
    precision = None

    # constructor
    def __init__(self, p_parameter):
        self.precision = p_parameter

    def background_colours(self, image):
        """
        returns a list of background colours.
        Background colours are selected based on the similarity to the
        most abundant colour, controlled by precision variable.
        """
        if image.getpalette():
            image = image.convert('RGB')
        # increasing the threshold of getcolors() method
        colors = image.getcolors(image.size[0] * image.size[1])
        colors.sort(key=lambda tup: tup[0], reverse=True)
        selected = []
        for f, c in colors:  # the most abundant colour assigned to the list
            selected.append(c)
            break
        # verifies if colour is an another hue of the background colour
        for index, (freq, colour) in enumerate(colors[1:]):
            if self.similarity(selected[0], colour):
                selected.append(colour)
            else:
                return selected

    def similarity(self, colour, c_colour):
        """
        returns true, when a given colour meets restriction (precision)
        Verifies each colour and checks if the given colour is similar or not.
        """
        if abs(colour[0] - c_colour[0]) <= int(self.precision):  # red
            if abs(colour[1] - c_colour[1]) <= int(self.precision):  # green
                if abs(colour[2] - c_colour[2]) <= int(self.precision):  # blue
                    return True
        else:
            return False
