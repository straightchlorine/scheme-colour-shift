from ColourConversion import colour_shift
from DirectoryTraversal import queue


def userinput():


def help_prompt():
    print("shift [-p] [-wt] [-bt] [[-i] or [-g]]\n\n" +
          "     -p          determines the tolerance of colours will be considered as background\n" +
          "     -wt         determines how close to white a colour must be in order to be considered white\n" +
          "     -bt         determiens how close to black a colour must be in order to be considered black\n")


def core():
    print(sys.argv)

core()
