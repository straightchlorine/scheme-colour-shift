import os
from PIL import ImageColor


def precision_validation(precision):
    if int(precision) < 0:
        print('!>> precision value cannot be negative')
        return False
    else:
        return True


def wt_validation(wt):
    if int(wt) > 255:
        print('!>> white threshold value exceeds 255')
        return False
    elif int(wt) < 0:
        print('!>> white threshold value cannot be negative')
        return False
    else:
        return True


def bt_validation(bt):
    if int(bt) > 255:
        print('!>> black threshold value exceeds 255')
        return False
    elif int(bt) < 0:
        print('!>> black threshold value cannot be negative')
        return False
    else:
        return True


def colour_validation(colour):
    try:
        buffer = ImageColor.getrgb(colour)
    except ValueError:
        print('!>> invalid colour ' + colour)
        return False
    return True;


def path_validation(path):
    if os.path.exists(path):
        if os.path.isdir(path):
            print('!>> specified path is a directory')
            return False
        else:
            return True
    else:
        print('!>> specified path does not exist')
        return True

