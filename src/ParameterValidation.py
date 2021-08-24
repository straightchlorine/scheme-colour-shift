import os
from PIL import ImageColor


class Validation:
    p_param = None
    wt_param = None
    bt_param = None
    mk_c_param = None
    bg_c_param = None
    fg_c_param = None
    path_param = None
    error_msg = None

    def __init__(self, parameters):
        self.p_param = parameters[0][1]
        self.wt_param = parameters[1][1]
        self.bt_param = parameters[2][1]
        self.mk_c_param = parameters[3][1]
        self.bg_c_param = parameters[4][1]
        self.fg_c_param = parameters[5][1]
        self.path_param = parameters[6][1]

    def validate(self):
        if (self.precision_validation() and
                self.wt_param_validation() and
                self.bt_validation() and
                self.colour_validation(self.mk_c_param) and
                self.colour_validation(self.bg_c_param) and
                self.colour_validation(self.fg_c_param) and
                self.path_validation()):

            print(self.error_msg)
            return True

        else:
            return False

    def precision_validation(self):
        if self.p_param < 0:
            self.error_msg = '!>> precision value cannot be negative'
            return False
        else:
            return True

    def wt_param_validation(self):
        if self.wt_param > 255:
            self.error_msg = '!>> white threshold value exceeds 255'
            return False
        elif self.wt_param < 0:
            self.error_msg = '!>> white threshold value cannot be negative'
            return False
        else:
            return True

    def bt_validation(self):
        if self.bt_param > 255:
            self.error_msg = '!>> black threshold value exceeds 255'
            return False
        elif self.bt_param < 0:
            self.error_msg = '!>> black threshold value cannot be negative'
            return False
        else:
            return True

    def colour_validation(self, colour):
        try:
            buffer = ImageColor.getrgb(colour)
        except ValueError:
            self.error_msg = '!>> invalid colour ' + colour
            return False
        return True

    def path_validation(self):
        self.path_param.replace('~', '/home/goldberg')

        if os.path.exists(self.path_param):
            if os.path.isdir(self.path_param):
                self.error_msg = '!>> specified path is a directory'
                return False
            else:
                return True
        else:
            self.error_msg = '!>> specified path does not exist'
            return True
