from ColourConversion import colour_shift
from DirectoryTraversal import queue


def cli():
    """
    returns void

    Main function of the application, provides a simple user interface.
    """
    input = user_input()

    # main loop
    while True:

        if input == 'exit' or input == 'quit':
            print("Program terminated.")
            break

        elif input == 'help':
            help_prompt()

        elif input.find('shift') != -1:
            parameters = parameter_scan(input)

            colour_shift(
                parameters[0][1],   # precision
                parameters[1][1],   # white threshold
                parameters[2][1],   # blach threshold
                parameters[3][1],   # mark colour
                parameters[4][1],   # foreground
                parameters[5][1],   # background
                parameters[6][1])   # directory

        else:
            print("Invalid command.")

        input = user_input()


def user_input():
    """
    Convenience method.
    """
    command = input(">> ")
    return command


def help_prompt():
    print("shift [-p] [-wt] [-bt] [-mk] [-fg] [-bg]\n\n" +
          "     -p          determines the range of colours considered as background\n" +
          "     -wt         determines how close to white a colour must be in order to be considered white\n" +
          "     -bt         determines how close to black a colour must be in order to be considered black\n" +
          "     -mk         marks colours not considered either a background or foreground ones\n" +
          "     -fg         determines which colour will replace foreground colours\n" +
          "     -bg         determines which colour will replace background colours\n" +
          "     exit        exit the program\n")


def parameter_scan(command):
    """
    returns a list of parameters, extracted from the command

    The list has a predetermined order, for the purpose of receiving
    arguments in various configurations.
    """

    # removing the prefix
    parameters = command.split(' ')
    parameters.pop(0)

    # obtaining the directory and removing it from the list
    directory = parameters[-1]
    parameters.pop(-1)

    # default parameters
    p_val = 50
    wt_val = 240
    bt_val = 30

    # default colouring
    bg_colour = 'white'
    fg_colour = 'black'
    mk_colour = 'red'

    val = []
    for index, parameter in enumerate(parameters):

        if parameter == '-p':
            p_val = parameters[index + 1]
        if parameter == '-wt':
            wt_val = parameters[index + 1]
        if parameter == '-bt':
            bt_val = parameters[index + 1]
        if parameter == '-mk':
            mk_colour = parameters[index + 1]
        if parameter == '-bg':
            bg_colour = parameters[index + 1]
        if parameter == '-fg':
            fg_colour = parameters[index + 1]

    # grouping parameters
    val.append(p_val)
    val.append(wt_val)
    val.append(bt_val)
    val.append(mk_colour)
    val.append(bg_colour)
    val.append(fg_colour)
    val.append(directory)

    # assigning each parameter an index
    params = []
    for index, param_value in enumerate(val):
        params.append((index, param_value))

    return params


cli()
