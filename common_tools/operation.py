from pyquil.quil import Program


def repeat_program(program, times):
    """
    repeats a pyquil program

    :param program: the program that should be repeated
    :param times: how many times should the program repeated

    :return: resulting times * program pyquil program
    """

    if times < 0:
        raise ValueError("negative numbers not allowed")
    if times == 0:
        return Program()

    return_program = Program()

    for index in range(0, times):
        return_program += program

    return return_program