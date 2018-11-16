from pyquil.parameters import Parameter, quil_sin, quil_cos, quil_exp
from pyquil.quilbase import DefGate
from math import sqrt
import numpy as np


def create_CRX():
    """
    Defining control RX pyquil Gate

    :return: instruction for CRX
    """

    theta = Parameter('theta')
    crx = np.array([[1, 0, 0, 0],
                    [0, 1, 0, 0],
                    [0, 0, quil_cos(theta / 2), -1j * quil_sin(theta / 2)],
                    [0, 0, -1j * quil_sin(theta / 2), quil_cos(theta / 2)]])

    dg = DefGate('CRX', crx, [theta])
    return dg


def create_CRZ():
    """
    Defining control RX pyquil Gate

    :return: instruction for CRZ
    """

    theta = Parameter('theta')
    crz = np.array([[1, 0, 0, 0],
                    [0, 1, 0, 0],
                    [0, 0, quil_exp(-1j*theta / 2), 0],
                    [0, 0, 0, quil_exp(1j*theta / 2)]])

    dg = DefGate('CRZ', crz, [theta])
    return dg


def create_CH():
    """
    Defining control RX pyquil Gate

    :return: instruction for CRZ
    """

    ch = np.array([[1, 0, 0, 0],
                    [0, 1, 0, 0],
                    [0, 0, 1/sqrt(2), 1/sqrt(2)],
                    [0, 0, 1/sqrt(2), -1/sqrt(2)]])

    dg = DefGate('CH', ch)
    return dg



