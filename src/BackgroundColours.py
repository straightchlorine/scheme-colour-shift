def backgroundcolours(image):
    """
    Finds most common colours and their hues in order to
    determine the background colours of the image.
    """

    if image.getpalette():              # procuring the list of colours
        image = image.convert('RGB')

    # increasing the threshold of getcolors() method
    colors = image.getcolors(image.size[0] * image.size[1]) 
    colors.sort(key=lambda tup: tup[0], reverse=True)

    selected = []

    for f, c in colors:  # the most abundant colour assigned to the list
        selected.append(c)
        break

    # verifies if colour is another hue of the background colour
    for index, (freq, colour) in enumerate(colors[1:]):
        if similarity(selected[0], colour):
            selected.append(colour)
        else:
            return selected


def similarity(colour, c_colour):
    """
    Relies on precision variable and determines how different
    is one colour from another.
    """
    precision = 100  # variable determines how much the colours are allowed to differ

    if abs(colour[0] - c_colour[0]) <= precision:           # red
        if abs(colour[1] - c_colour[1]) <= precision:       # green
            if abs(colour[2] - c_colour[2]) <= precision:   # blue
                return True
    else:
        return False
