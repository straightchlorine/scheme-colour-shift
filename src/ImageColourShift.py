from ColourConversion import colour_shift
from DirectoryTraversal import queue


def cli():
    input = user_input()
    while True:
        if input == 'exit' or input == 'quit':
            break
        variables = parameter_scan(input)
        colour_shift(variables[-1][1], variables[-2][1], variables[-3][1], variables[-4][1])
        break


def user_input():
    command = input(">> ")
    return command


def help_prompt():
    print("shift [-p] [-wt] [-bt] [[-i] or [-g]]\n\n" +
          "     -p          determines the tolerance of colours will be considered as background\n" +
          "     -wt         determines how close to white a colour must be in order to be considered white\n" +
          "     -bt         determines how close to black a colour must be in order to be considered black\n" +
          "     exit        exit the program")


def parameter_scan(command):
    if command.find('-p'):
        parameters = command.split(' ')
        parameters.pop(0)

        directory = parameters[-1]
        parameters.pop(-1)

        p_val = 50
        wt_val = 240
        bt_val = 30

        val = []
        for index, parameter in enumerate(parameters):
            parameter = parameter.rstrip()
            if parameter.isdecimal():
                continue

            if parameter == '-p':
                p_val = parameters[index + 1]

            if parameter == '-wt':
                wt_val = parameters[index + 1]

            bt_val = 20
            if parameter == '-bt':
                bt_val = parameters[index + 1]

        precision = (0, p_val)
        val.append(precision)

        white_threshold = (1, wt_val)
        val.append(white_threshold)

        black_threshold = (2, bt_val)
        val.append(black_threshold)

        dir_param = (3, directory)
        val.append(dir_param)

        return val


cli()
