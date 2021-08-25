from ColourConversion import Conversion
from ParameterData import ParameterData


class CLI:
    """
    Main class of the program, essentially wraps everything together and
    provides really basic user interface.
    """
    u_input = None

    def __init__(self):
        self.cli()

    def cli(self):
        """
        returns void

        Main function of the application, provides a simple user interface.
        """
        self.user_input()

        # main loop
        while True:

            if self.u_input == 'exit' or self.u_input == 'quit':
                print("#>> program terminated.")
                break

            elif self.u_input == 'help':
                help_prompt()

            elif self.u_input.find('shift') != -1:
                if not self.shift_command():
                    continue

            elif self.u_input == '':
                self.user_input()
                continue

            else:
                print('!>> invalid command')

            self.user_input()

    def user_input(self):
        """
        Convenience method.
        """
        self.u_input = input(">> ")
        return self.u_input

    def shift_command(self):
        """
        returns false if the validation was not a success
        """
        parameters = ParameterData(parameter_scan(self.u_input))

        if not parameters.validate():
            self.u_input = ''
            return False

        shift = Conversion(parameters)
        shift.colour_shift()
        return True


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

        # extracting the values
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


if __name__ == '__main__':
    cli = CLI()
