from ParameterValidation import Validation


class ParameterData:
    """
    Storage class responsible for holding data extracted from the command.
    """
    p_param = None
    wt_param = None
    bt_param = None
    mk_c_param = None
    bg_c_param = None
    fg_c_param = None
    path_param = None

    val = None  # validation object

    def __init__(self, parameters):
        self.p_param = int(parameters[0][1])
        self.wt_param = int(parameters[1][1])
        self.bt_param = int(parameters[2][1])
        self.mk_c_param = parameters[3][1]
        self.bg_c_param = parameters[4][1]
        self.fg_c_param = parameters[5][1]
        self.path_param = parameters[6][1]
        self.val = Validation(self)

    def validate(self):
        if (self.val.precision_validation() and
                self.val.wt_param_validation() and
                self.val.bt_validation() and
                self.val.colour_validation(self.mk_c_param) and
                self.val.colour_validation(self.bg_c_param) and
                self.val.colour_validation(self.fg_c_param) and
                self.val.path_validation()):
            return True
        else:
            print(self.val.error_msg)
            return False

    def get_error_msg(self):
        return self.val.error_msg
