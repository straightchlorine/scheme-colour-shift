from ColourConversion import colour_shift
from DirectoryTraversal import queue


def cli():
    """
    Main function of the application, provides a simple user interface.
    """
    input = user_input()

    while True:

        if input == 'exit' or input == 'quit':
            print("Program terminated.")
            break

        elif input == 'help':
            help_prompt()

        elif input.find('shift') != -1:
            parameters = parameter_scan(input)

            colour_shift(
                    parameters[-1][1],   # path
                    parameters[-2][1],   # background replacement colour
                    parameters[-3][1],   # foreground replacement colour
                    parameters[-4][1],   # mark colour (neither foreground or background) 
                    parameters[-5][1],   # black threshold 
                    parameters[-6][1],   # white threshold
                    parameters[-7][1]    # precision
                    )
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
    print("shift [-p] [-wt] [-bt] [-mkc] [-fgc] [-bgc]\n\n" +
          "     -p          determines the range of colours considered as background\n" +
          "     -wt         determines how close to white a colour must be in order to be considered white\n" +
          "     -bt         determines how close to black a colour must be in order to be considered black\n" +
          "     -mkc        colour, which marks colours not considered either a background or foreground ones\n" +
          "     -fgc        determines, which colour will replace foreground colours\n" +
          "     -bgc        determines, which colour will replace background colours\n" +
          "     exit        exit the program\n")


def parameter_scan(command):
    """
    Function extracts the values of each parameter of the command,
    and assigns them to the single list as tuples, in predetermined
    order.
    """
    parameters = command.split(' ')
    parameters.pop(0)

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

        parameter = parameter.rstrip()

        if parameter.isdecimal():
            continue

        if parameter == '-p':
            p_val = parameters[index + 1]

        if parameter == '-wt':
            wt_val = parameters[index + 1]

        if parameter == '-bt':
            bt_val = parameters[index + 1]

        if parameter == '-mkc':
            mk_colour = parameters[index + 1]

        if parameter == '-bgc':
            bg_colour = parameters[index + 1]

        if parameter == '-fgc':
            fg_colour = parameters[index + 1]

    precision = (0, p_val)
    val.append(precision)

    white_threshold = (1, wt_val)
    val.append(white_threshold)

    black_threshold = (2, bt_val)
    val.append(black_threshold)

    mark_colour = (3, mk_colour)
    val.append(mark_colour)

    foreground_colour = (4, fg_colour)
    val.append(foreground_colour)

    background_colour = (5, bg_colour)
    val.append(background_colour)

    dir_param = (6, directory)
    val.append(dir_param)

    return val


cli()
