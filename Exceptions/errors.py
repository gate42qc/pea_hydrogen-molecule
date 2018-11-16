class RIGETTI_SERVER_ERROR(Exception):
    """
    Sometimes Rigetti server doesn't work and the server
    raises some errors, that we are handling somehow. But
    when the it becomes hard to handle server errors we should
    raise this error.
    """

    def __init__(self, arg):
        self.strerror = arg
        self.args = {arg}


class NotGateException(Exception):
    """
    raise this exception when you don't have desired pyquil's Gate object
    """

    def __init__(self, arg):
        self.strerror = arg
        self.args = {arg}


class LogicException(Exception):
    """
    If you got something wrong in the code that is most probably due to some
    logic error then use this exception
    """

    def __init__(self, arg):
        self.strerror = arg
        self.args = {arg}