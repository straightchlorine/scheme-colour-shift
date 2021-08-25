import os
from PIL import ImageColor


class Validation:
    """
    Class responsible for verifying if given parameters are indeed valid.
    """
    param_data = None
    error_msg = None

    def __init__(self, params):
        self.param_data = params

    def precision_validation(self):
        if self.param_data.p_param < 0:
            self.error_msg = '!>> precision value cannot be negative'
            return False
        else:
            return True

    def wt_param_validation(self):
        if self.param_data.wt_param > 255:
            self.error_msg = '!>> white threshold value exceeds 255'
            return False
        elif self.param_data.wt_param < 0:
            self.error_msg = '!>> white threshold value cannot be negative'
            return False
        else:
            return True

    def bt_validation(self):
        if self.param_data.bt_param > 255:
            self.error_msg = '!>> black threshold value exceeds 255'
            return False
        elif self.param_data.bt_param < 0:
            self.error_msg = '!>> black threshold value cannot be negative'
            return False
        else:
            return True

    def colour_validation(self, colour):
        try:
            ImageColor.getrgb(colour)
        except ValueError:
            self.error_msg = '!>> invalid colour ' + colour
            return False
        return True

    def path_validation(self):
        self.param_data.path_param.replace('~', '/home/goldberg')

        if os.path.exists(self.param_data.path_param):
            if os.path.isdir(self.param_data.path_param):
                self.error_msg = '!>> specified path is a directory'
                return False
            else:
                return True
        else:
            self.error_msg = '!>> specified path does not exist'
            return True
